import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = '<NAME>'  # who is sending this email
email['to'] = 'na@na.com'  # email id for which you want to send the email
email['subject'] = 'you won 100 dollars!'  # body of the email

email.set_content('I am a python master!')  # kinda header

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # login to email id from which you want to send an email and password
    smtp.login('na@na.com', 'password')
    smtp.send_message(email)
    print('all good boss')
