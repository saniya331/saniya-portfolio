# app.py - Main Flask application for Student Portfolio Website

from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# ─── Route: Home Page ────────────────────────────────────────────────────────
@app.route("/")
def home():
    """Render the main portfolio page."""
    return render_template("index.html")


# ─── Route: Contact Form Submission ──────────────────────────────────────────
@app.route("/contact", methods=["POST"])
def contact():
    """
    Handle contact form submission.
    Reads name and email from the form, then renders a thank-you page.
    """
    name  = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    # Basic validation
    if not name or not email:
        return render_template("index.html", error="Please fill in both fields.")

    # Render thank-you message (passed as template variables)
    return render_template("thankyou.html", name=name, email=email)


# ─── Run the development server ───────────────────────────────────────────────
if __name__ == "__main__":
    # debug=True auto-reloads on code changes (disable in production)
    app.run(debug=True)
