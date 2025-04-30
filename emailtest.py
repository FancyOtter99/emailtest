import smtplib
from email.message import EmailMessage

smtp_host = "smtp-relay.brevo.com"
smtp_port = 587
smtp_user = "8bbf44001@smtp-brevo.com"
smtp_pass = "cQFX2xCp1794DWY3"

msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = smtp_user
msg["To"] = "alexwasbest@gmail.com"
msg.set_content("This is a test.")

try:
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.set_debuglevel(1)  # ← see what's happening
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        print("Sent!")
except Exception as e:
    print("FAILED:", e)
