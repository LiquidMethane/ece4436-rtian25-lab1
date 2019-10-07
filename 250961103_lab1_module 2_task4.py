import smtplib
import getpass

mailserver = 'smtp-mail.outlook.com'
port = 587

msg = '\r\nRuiqi Tian (rtian25) 250961103'

username = 'richy990113@hotmail.com'
password = getpass.getpass('Password: ')
rcpt = 'manidimi123123@hotmail.com'

messageHeader = ["From: " + username, "Subject: Test client using smtplib", "To: " + rcpt, "MIME-Version: 1.0", "Content-Type: text"]
messageHeader = "\r\n".join(messageHeader)
print('Initializing sendEmail sequence......')

connection = smtplib.SMTP(mailserver, port)

connection.ehlo()

connection.starttls()

connection.ehlo()

connection.login(username, password)

connection.sendmail(username, rcpt, messageHeader + '\r\n' + msg)

connection.quit()

print('Email sent.')
