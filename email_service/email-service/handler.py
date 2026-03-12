import json
import smtplib
from email.mime.text import MIMEText

def sendEmail(event, context):

    print("Lambda triggered")

    body = json.loads(event.get("body", "{}"))

    action = body.get("action")
    email = body.get("email")

    print("Action:", action)
    print("Target email:", email)

    if action == "BOOKING_CONFIRMATION":
        subject = "Booking Confirmation"
        message = "Your hospital appointment has been successfully booked."
    elif action == "SIGNUP_WELCOME":
        subject = "Welcome to HMS"
        message = "Welcome to the Hospital Management System."
    else:
        subject = "Notification"
        message = "Hello from HMS."

    sender_email = "mdkaifznkhi@gmail.com"
    sender_password = "vcjultudixvmufds"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    try:
        print("Connecting to Gmail SMTP...")

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)

        print("Login successful")

        server.sendmail(sender_email, email, msg.as_string())

        print("Email sent successfully")

        server.quit()

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully"})
        }

    except Exception as e:
        print("Email error:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }