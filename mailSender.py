import smtplib
import getpass

mailserver = 'smtp-mail.outlook.com'
port = 587

username = input("Username: ")
password = getpass.getpass('Password: ')
rcpt = input("Recipient: ")

messageHeader = ["From: " + username, "Subject: Test client using smtplib", "To: " + rcpt, "MIME-Version: 1.0", "Content-Type: text"]
messageHeader = "\r\n".join(messageHeader)
print('now sending email...')

connection = smtplib.SMTP(mailserver, port)
connection.ehlo()
connection.starttls()
connection.ehlo()
connection.login(username, password)
connection.sendmail(username, rcpt, messageHeader + '\r\n\r\n I love computer networks!')
connection.quit()
