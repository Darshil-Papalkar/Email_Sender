import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Darshil Papalkar'
email['to'] = 'papalkardarshil13@gmail.com'
email['subject'] = 'You are genius'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    file = open('C:\\Users\\DARSHIL\\OneDrive_1\\OneDrive\\Desktop\\python-Voice Recognizer\\JARVIS\\pwd.txt', 'r')
    smtp.login('papalkardarshil12@gmail.com', file.readline())
    smtp.send_message(email)
    print("All Done!")
