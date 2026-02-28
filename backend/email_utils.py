

# import smtplib
# from email.message import EmailMessage
# import os
# from dotenv import load_dotenv

# load_dotenv()

# MAIL_USERNAME = os.getenv("23b01a12c4@svecw.edu.in")
# MAIL_PASSWORD = os.getenv("seib bsel vnsa eama")
# MAIL_SERVER = os.getenv("smtp.gmail.com")
# MAIL_PORT = int(os.getenv("587"))
# MAIL_FROM_NAME = os.getenv("Srivalli")


# async def send_booking_email(to_email, subject, message, attachment_path=None):
#     msg = EmailMessage()
#     msg["From"] = f"{MAIL_FROM_NAME} <{MAIL_USERNAME}>"
#     msg["To"] = to_email
#     msg["Subject"] = subject
#     msg.set_content(message)

#     # Attach PDF if exists
#     if attachment_path:
#         with open(attachment_path, "rb") as f:
#             file_data = f.read()
#             file_name = os.path.basename(attachment_path)

#         msg.add_attachment(
#             file_data,
#             maintype="application",
#             subtype="pdf",
#             filename=file_name,
#         )

#     try:
#         with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
#             server.starttls()  # 🔥 IMPORTANT
#             server.login(MAIL_USERNAME, MAIL_PASSWORD)
#             server.send_message(msg)
#             print(f"✅ Email sent to {to_email}")

#     except Exception as e:
#         print("❌ Email sending failed:", str(e))


import smtplib
from email.message import EmailMessage
import os

# Direct values (simplest & safest for now)
MAIL_USERNAME = "23b01a12c4@svecw.edu.in"
MAIL_PASSWORD = "seib bsel vnsa eama"   # App password
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_FROM_NAME = "Srivalli"


async def send_booking_email(to_email, subject, message, attachment_path=None):
    msg = EmailMessage()
    msg["From"] = f"{MAIL_FROM_NAME} <{MAIL_USERNAME}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(message)

    # Attach PDF if exists
    if attachment_path:
        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename=file_name,
        )

    try:
        with smtplib.SMTP(MAIL_SERVER, MAIL_PORT) as server:
            server.starttls()
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            server.send_message(msg)
            print(f"✅ Email sent to {to_email}")

    except Exception as e:
        print("❌ Email sending failed:", str(e))