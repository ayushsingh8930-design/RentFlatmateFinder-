import smtplib
from email.mime.text import MIMEText

from app.config import settings


def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = settings.EMAIL_USERNAME
    msg["To"] = to_email

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.starttls()
        server.login(
            settings.EMAIL_USERNAME,
            settings.EMAIL_PASSWORD
        )
        server.send_message(msg)

    print(f"Email sent to {to_email}")