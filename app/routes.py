# app/routes.py

from flask import Blueprint, render_template, request, session
from .utils import handle_user_input
from datetime import timedelta

main = Blueprint("main", __name__)

@main.before_app_request
def setup_session():
    """Ensure session is persistent and initialized."""
    session.permanent = True
    session.modified = True
    session.permanent_session_lifetime = timedelta(minutes=10)

    if "state" not in session:
        session["state"] = "main_menu"

    if "chat_log" not in session:
        session["chat_log"] = []

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            session["chat_log"].append(("You", user_input))
            response = handle_user_input(user_input)
            session["chat_log"].append(("SafeSathi", response))

    return render_template("layout.html", chat_log=session["chat_log"])
