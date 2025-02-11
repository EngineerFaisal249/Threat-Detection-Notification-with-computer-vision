import smtplib

def send_email_with_image(smtp_server, port, sender_email, password, receiver_email, subject, body, image_path=None):
    server = None
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Optional, used to identify the client to the server
        server.starttls()  # Secure the connection
        server.ehlo()  # Optional
        server.login(sender_email, password)
        
        # Send email
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        if server:
            server.quit()

# Usage
smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'shahfaisal15401@gmail.com'
password = 'Sh806784@#'  # Use an app password instead of your main password
receiver_email = 'shahfaisal15401@gmail.com'
subject = 'Test Email'
body = 'This is a test email from Python script.'

send_email_with_image(smtp_server, port, sender_email, password, receiver_email, subject, body)
