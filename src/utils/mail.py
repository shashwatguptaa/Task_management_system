from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List

conf = ConnectionConfig(
    MAIL_USERNAME = "test@gmail.com",
    MAIL_PASSWORD = ""
    MAIL_FROM = "test@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp. gmail.com",
    MAIL_FROM_NAME="Test"
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

async def send_email(email: List[str]):
    html = """<p>Hi this test mail, thanks for using Fastapi-mail</p> """

    message = MessageSchema (
    subject="Fastapi-Mail module",
    # recipients=email.dict().get("email"),
    recipients=email,
    body=html,
    subtype=MessageType.html)

    fm = FastMail(conf)
    await fm. send_message (message)
    return {"message": "email has been sent successfully"}