import smtplib
import getpass

# define mailserver and port number

mailserver = 'smtp-mail.outlook.com'
port = 587

# dynamic username, password and recipient input

username = input("Username: ")
password = getpass.getpass('Password: ')
rcpt = input("Recipient: ")

# construct message header

messageHeader = ["From: " + username, "Subject: Test client using smtplib", "To: " + rcpt, "MIME-Version: 1.0", "Content-Type: text"]
messageHeader = "\r\n".join(messageHeader)
print('now sending email...')

# establish connection with mailserver
connection = smtplib.SMTP(mailserver, port)

# send EHLO command
connection.ehlo()

# send STARTTLS command
connection.starttls()

# send EHLO command again
connection.ehlo()

# login with credential
connection.login(username, password)

# send email
connection.sendmail(username, rcpt, messageHeader + '\r\n\r\n I love computer networks!')

# close connection
connection.quit()
