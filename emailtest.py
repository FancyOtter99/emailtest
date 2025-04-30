import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Zoho SMTP Server details
smtp_server = "smtp.zoho.com"
smtp_port = 587  # or use 465 for SSL
smtp_username = "fancyotter99@fancyotter99.run.place"
smtp_password = "ZfxLRnvpmLcK"  # If using 2FA

# Email content
from_address = "fancyotter99@fancyotter99.run.place"
to_address = "pizza.great@protonmail.com"
subject = "Test Email from Zoho"
body = "This is a test email sent from Zoho Mail."

# Create the email
message = MIMEMultipart()
message["From"] = from_address
message["To"] = to_address
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # For TLS encryption
    server.login(smtp_username, smtp_password)
    text = message.as_string()
    server.sendmail(from_address, to_address, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()

