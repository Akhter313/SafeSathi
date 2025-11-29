# app/routes.py

from flask import Blueprint, render_template, request, session, jsonify
from .utils import handle_user_input, get_text
from datetime import timedelta

main = Blueprint("main", __name__)

@main.before_app_request
def setup_session():
    """Ensure session is persistent and initialized."""
    session.permanent = True
    session.modified = True
    session.permanent_session_lifetime = timedelta(minutes=10)

    if "state" not in session:
        session["state"] = "language_selection_init" # Start with language selection
    
    if "chat_log" not in session:
        session["chat_log"] = []
    
    if "lang" not in session:
        session["lang"] = "en"

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            session["chat_log"].append(("You", user_input))
            response = handle_user_input(user_input)
            session["chat_log"].append(("SafeSathi", response))

    return render_template("layout.html", chat_log=session.get("chat_log", []))

@main.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = handle_user_input(user_input)
    return jsonify({"response": response})

@main.route("/select-language", methods=["GET"])
def select_language_options():
    """Returns the available languages for the modal."""
    options = [
        {"code": "en", "label": "English"},
        {"code": "hi", "label": "हिंदी (Hindi)"},
        {"code": "ur", "label": "اردو (Urdu)"}
    ]
    return jsonify(options)

@main.route("/set-language/<lang_code>", methods=["POST"])
def set_language(lang_code):
    """Sets the language in session and returns the welcome message."""
    if lang_code in ["en", "hi", "ur"]:
        session["lang"] = lang_code
        session["state"] = "main_menu"
        
        # Get welcome message in selected language
        welcome_msg = get_text(lang_code, "welcome_after_lang")
        menu_msg = get_text(lang_code, "menu")
        
        return jsonify({"response": welcome_msg + "\n\n" + menu_msg})
    
    return jsonify({"error": "Invalid language"}), 400

@main.route("/get-menu-options", methods=["GET"])
def get_menu_options():
    """Returns the menu options for the modal."""
    lang = session.get("lang", "en")
    
    # Get menu text and parse it
    menu_text = get_text(lang, "menu")
    
    # Parse menu options
    options = []
    lines = menu_text.split("\n")
    for line in lines:
        if line.strip() and line[0].isdigit():
            # Extract number and label
            parts = line.split(".", 1)
            if len(parts) == 2:
                num = parts[0].strip()
                label = parts[1].strip()
                options.append({"value": num, "label": f"{num}. {label}"})
    
    return jsonify(options)

@main.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():
    """
    Mock webhook for WhatsApp integration.
    """
    data = request.json
    print(f"Received WhatsApp webhook: {data}")
    return jsonify({"status": "received"}), 200
