import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from unicodedata import name  # os.path to access html path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'sender@email'
email['to'] = 'receipient@email'
email['subject'] = 'Yayyy, first scripting project using python to send email'

#email.set_content('I am a Python Master!')
email.set_content(html.substitute({'name': 'Rayray'}),'html')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('me@email', 'me@password)
    smtp.send_message(email)
    print('all good boss !')
