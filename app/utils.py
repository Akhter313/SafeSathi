# app/utils.py

from flask import session
from app.texts import get_text
from app.ai.cohere_gpt import generate_response
from app.ai.local_models import predict_url
from app.ai.local_models.text_model import predict_text
from app.logs import log_interaction


def append_menu_select(response, lang):
    """Append menu select prompt to response"""
    menu_prompt = get_text(lang, "menu_select_prompt")
    return response + menu_prompt

def handle_user_input(user_input):
    """
    Core chatbot logic.
    Handles user input based on session state and returns a response.
    """
    user_input_lower = user_input.lower().strip()
    
    # Initialize language if not set
    if "lang" not in session:
        session["lang"] = "en" # Default to English
        session["state"] = "language_selection_init"
        return get_text("en", "welcome_card")

    lang = session["lang"]
    state = session.get("state", "main_menu")

    # Global commands
    if user_input_lower in ["menu", "hi", "hello", "start"]:
        session["state"] = "language_selection_init"
        return get_text("en", "welcome_card")
    
    if user_input_lower == "lang":
        session["state"] = "language_selection_init"
        return get_text("en", "welcome_card")

    # State: Language Selection Init (Waiting for user to click Select)
    if state == "language_selection_init":
        pass 

    # State: Main Menu
    if state == "main_menu":
        if user_input_lower == "1":
            session["state"] = "awaiting_link"
            return get_text(lang, "awaiting_link")  # No menu select here
        
        elif user_input_lower == "2":
            session["state"] = "awaiting_report"
            return get_text(lang, "awaiting_report")  # No menu select here
        
        elif user_input_lower in ["3", "tips", "tip"]:
            return append_menu_select(get_text(lang, "tip"), lang)  # Add menu select after tip
        
        elif user_input_lower == "4":
            session["state"] = "reporting_scam"
            return get_text(lang, "report_init")  # No menu select here - just asking what happened
        
        elif user_input_lower == "5":
            return append_menu_select(get_text(lang, "alerts"), lang)  # Add menu select after alerts
        
        elif user_input_lower == "6":
            return append_menu_select(get_text(lang, "blog"), lang)  # Add menu select after blog
        
        elif user_input_lower == "7":
            return append_menu_select(get_text(lang, "checklist"), lang)  # Add menu select after checklist
        
        elif user_input_lower == "8":
            return append_menu_select(get_text(lang, "reporting_sites"), lang)  # Add menu select after sites
        
        elif user_input_lower == "9":
            session.clear()
            return get_text(lang, "exit")
        
        else:
            if len(user_input.split()) > 2:
                 ai_reply = generate_response(user_input)
                 log_interaction(user_input, ai_reply)
                 return append_menu_select(ai_reply + get_text(lang, "return_menu"), lang)
            
            return append_menu_select(get_text(lang, "unknown"), lang)

    # State: Awaiting Link
    elif state == "awaiting_link":
        session["state"] = "main_menu"
        result = predict_url(user_input)
        label_key = result["label"]
        label_text = get_text(lang, label_key)
        
        reply = get_text(lang, "scan_result", url=user_input, label=label_text, prob=result["prob"])
        
        if result.get("suggestion"):
            reply += "\n\n" + get_text(lang, "did_you_mean", suggestion=result['suggestion']) + "\n"
            if "https://" in result['suggestion'] and "http://" in user_input:
                 reply += get_text(lang, "http_insecure")
            else:
                 reply += get_text(lang, "typo_format")

        if result["label"] != "safe":
             if user_input.startswith("http://") and result["prob"] == 0.75:
                 reply += "\n\n" + get_text(lang, "http_risk")
             else:
                 reply += "\n\n" + get_text(lang, "risk_warning")
        
        return append_menu_select(reply + get_text(lang, "return_menu"), lang)  # Add menu select after result


    # State: Awaiting Report (Scam Text Check)
    elif state == "awaiting_report":
        session["state"] = "main_menu"
        result = predict_text(user_input)
        label_key = result["label"]
        label_text = get_text(lang, label_key)
        
        reply = get_text(lang, "scam_result", label=label_text, prob=result["prob"])
        
        if result["label"] == "scam":
            reply += "\n\n" + get_text(lang, "scam_detected_footer")
        else:
            reply += "\n\n" + get_text(lang, "safe_footer")
        
        return append_menu_select(reply + get_text(lang, "return_menu"), lang)  # Add menu select after result

    # State: Reporting Scam (Interactive)
    elif state == "reporting_scam":
        session["state"] = "main_menu"
        
        from app.ai.scam_guidance import detect_scam_type, generate_scam_guidance
        
        scam_type = detect_scam_type(user_input)
        result = predict_text(user_input)
        label = result["label"]
        
        guidance = generate_scam_guidance(user_input, label, scam_type, lang)
        final_reply = guidance + "\n\n" + get_text(lang, "helpline")
        
        return append_menu_select(final_reply, lang)  # Add menu select AFTER giving guidance

    return append_menu_select(get_text(lang, "unknown"), lang)
