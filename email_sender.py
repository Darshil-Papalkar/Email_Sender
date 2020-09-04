import smtplib
from email.message import EmailMessage

email = EmailMessage()
# Sender's name
email['from'] = 'Darshil Papalkar'
# Receiver's mail id
email['to'] = 'receiver@gmail.com'
#  Email Subject
email['subject'] = 'SUBJECT'
# Email Content
email.set_content('CONTENT')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
#     Create a text document and store password
    file = open('text\\document\\pwd.txt', 'r')
    smtp.login('sender@gmail.com', file.readline())
    smtp.send_message(email)
print("All Done!")
