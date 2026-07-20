# app.py - Main Flask application for Student Portfolio Website
import os
import resend
from flask import Flask, render_template, request
resend.api_key = os.getenv("RESEND_API_KEY")
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

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "index.html",
            error="Please fill in all fields."
        )

    try:
        resend.Emails.send({
            "from": "Portfolio <onboarding@resend.dev>",
            "to": "saniyabegum.tech@gmail.com",   # Replace with your email if different
            "subject": f"New Portfolio Contact from {name}",
            "html": f"""
                <h2>New Contact Form Submission</h2>

                <p><strong>Name:</strong> {name}</p>

                <p><strong>Email:</strong> {email}</p>

                <p><strong>Message:</strong> {message}</p>
            """
        })

        return render_template(
    "index.html",
    success="Your message has been sent successfully!"
)

    except Exception as e:
        return render_template(
            "index.html",
            error=f"Failed to send message: {e}"
        )


# ─── Run the development server ───────────────────────────────────────────────
if __name__ == "__main__":
    # debug=True auto-reloads on code changes (disable in production)
    app.run(debug=True)
