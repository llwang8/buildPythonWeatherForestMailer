import smtplib

def send_emails(emails, schedule, forecast):
    # connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    # Start TLS encryption
    server.starttls()
    #login
    password = input("What's your password?")
    from_email = 'wangxbl56@gmail.com' #  needs a email
    server.login(from_email, password)

    # Send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the Cirus:\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Hope to see you there!'
        server.sendmail(from_email, to_email, message)


    server.quit()




