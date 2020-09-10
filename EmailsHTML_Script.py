import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = 'Dashline Dsouza'
email['to'] = '1decchu14@gmail.com'
email['subject'] = 'you won 100 dollars!'

email.set_content(html.substitute({'name': 'LinSoo'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('1jilinsoo14@gmail.com', '1jilinsoo14@')
    smtp.send_message(email)
    print('all good boss')
