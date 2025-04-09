# app/utils.py
from flask import session
from app.ai.cohere_gpt import generate_response
from app.logs import log_interaction

def handle_user_input(user_input):
    user_input_lower = user_input.lower()

    # Entry point
    if user_input_lower in ["hi", "menu"]:
        session["state"] = "main_menu"
        return (
            "✅ Main Menu:\n"
            "1. Check Suspicious Link\n"
            "2. Daily Cyber Tip\n"
            "3. Report a Scam\n"
            "4. Helpline & Support\n"
            "5. Latest Scam Alerts\n"
            "6. Awareness Blog\n"
            "7. Ask SafeSathi (AI)\n"
            "8. Safety Checklist\n"
            "9. Scam Reporting Sites\n"
            "0. Exit"
        )

    # Suspicious Link
    elif user_input_lower == "1" and session.get("state") == "main_menu":
        session["state"] = "awaiting_link"
        return "🔗 Please paste the suspicious link you'd like me to check."

    elif session.get("state") == "awaiting_link" and user_input_lower.startswith("http"):
        session["state"] = "main_menu"
        return f"⚠️ Scanning complete! This link may be unsafe: {user_input}\n\nType 'menu' to see options again."

    # Cyber Tip
    elif user_input_lower in ["2", "tips", "cyber tip", "tip"]:
        return "💡 Cyber Tip: Never trust links sent by strangers or unknown numbers. Type 'menu' to return."

    # Report Scam
    elif user_input_lower == "3":
        session["state"] = "awaiting_report"
        return "📩 Please paste the scam message or type your complaint:"

    elif session.get("state") == "awaiting_report":
        session["state"] = "main_menu"
        return (
            "✅ Thank you. Your report is logged.\n"
            "You can also visit https://cybercrime.gov.in or call 1930.\n\nType 'menu' to continue."
        )

    # Helpline
    elif user_input_lower == "4":
        return "📞 Cybercrime Helpline: Call 1930\nPortal: https://www.cybercrime.gov.in\nType 'menu' to return."

    # Scam Alerts
    elif user_input_lower == "5":
        return (
            "🚨 Trending Scam Alerts:\n"
            "- QR Code frauds\n"
            "- Fake job offers\n"
            "- WhatsApp impersonation\n"
            "- Investment scams\n\nType 'menu' to return."
        )

    # Awareness Blog
    elif user_input_lower == "6":
        return "📚 Visit: https://safesathi.blog for helpful blogs and guides. Type 'menu' to return."

    # GPT Chat Mode
    elif user_input_lower.startswith("chat:") or user_input_lower == "7":
        session["state"] = "main_menu"
        query = user_input[5:].strip() if user_input_lower.startswith("chat:") else "Tell me how to stay safe online."
        ai_reply = generate_response(query)
        log_interaction(query, ai_reply)
        return ai_reply + "\n\nType 'menu' to return."

    # Safety Checklist
    elif user_input_lower == "8":
        return (
            "✅ Online Safety Checklist:\n"
            "✔️ Use strong, unique passwords\n"
            "✔️ Enable 2FA on accounts\n"
            "✔️ Avoid public WiFi for sensitive tasks\n"
            "✔️ Verify links before clicking\n"
            "✔️ Don't overshare on social media\n\nType 'menu' to return."
        )

    # Trusted Links for Reporting
    elif user_input_lower == "9":
        return (
            "🌐 Trusted Cybercrime Portals:\n"
            "- Cybercrime Portal: https://www.cybercrime.gov.in\n"
            "- CERT-IN: https://www.cert-in.org.in\n"
            "- Twitter CyberDost: https://twitter.com/cyberdost\n\nType 'menu' to return."
        )

    # Exit
    elif user_input_lower == "0":
        session["state"] = "main_menu"
        return "👋 Thank you for using SafeSathi. Stay alert and stay safe!"

    # Unknown
    else:
        log_interaction(user_input, "❓ Unrecognized input.")
        return (
            "🤖 I'm still learning! Try:\n"
            "- 'menu' to see options\n"
            "- or 'chat: your question' to ask SafeSathi\n\nExample: chat: How to avoid phishing?"
        )
