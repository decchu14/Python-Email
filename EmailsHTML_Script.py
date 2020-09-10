import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

# here by using Path of pathlib route to index.html file and by using Template of string convert it into template form..
html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = '<NAME>'  # who is sending this email
email['to'] = 'na@na.com'  # email id for which you want to send the email
email['subject'] = 'you won 100 dollars!'  # body of the email

# here you will substitute the dynamic variables to
email.set_content(html.substitute({'name': 'Some_Name'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # login to email id from which you want to send an email and password
    smtp.login('na@na.com', 'password')
    smtp.send_message(email)
    print('all good boss')
