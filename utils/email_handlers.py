import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email

def send_email(to_email, subject, body):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    FROM_EMAIL = 'your_email@gmail.com'
    PASSWORD = 'your_app_password'
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)
        message = MIMEMultipart()
        message['From'] = FROM_EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(FROM_EMAIL, to_email, message.as_string())
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

def receive_emails():
    # Example IMAP connection to Gmail (adjust as necessary)
    IMAP_SERVER = 'imap.gmail.com'
    EMAIL_ACCOUNT = 'your_email@gmail.com'
    PASSWORD = 'your_app_password'

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, PASSWORD)
        mail.select('inbox')

        # Fetch latest email
        result, data = mail.search(None, 'ALL')
        email_ids = data[0].split()
        latest_email_id = email_ids[-1]
        
        result, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        
        return msg
    except Exception as e:
        return f"Failed to retrieve emails: {str(e)}"
