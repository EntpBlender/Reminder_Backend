def main():
    import smtplib
    import Verify
    import os
    MyEmailPassword = os.environ['MyEmailPassword']
    MyEmail = os.environ['MyEmail']

    from email.message import EmailMessage

    EmailTitle = input("What do you want the title of the email to be?\n|> ")
    EmailBody = input("What do you want the email body to be?\n|> ")
    EmailRecipient = input("Who do you want to send the email to?\n|> ")

    Email_Address = MyEmail
    EMAIL_PASSWORD = MyEmailPassword
    msg = EmailMessage()
    msg['Subject'] = EmailTitle
    msg['From'] = Email_Address
    msg['To'] = EmailRecipient
    msg.set_content(EmailBody)

    EmailValid = Verify.ValidateEmail(EmailRecipient)

    if EmailValid == True:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Email_Address, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email Sent")
    else:
        print("Email Not Sent")


if __name__ == "__main__":
    main()
