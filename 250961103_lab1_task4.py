import smtplib
import getpass

# define mailserver and port number

mailserver = 'smtp-mail.outlook.com'
port = 587

msg = '\r\nRuiqi Tian (rtian25) 250961103'

# dynamic username, password and recipient input

username = 'richy990113@hotmail.com'
password = getpass.getpass('Password: ')
rcpt = 'manidimi123123@hotmail.com'

# construct message header

messageHeader = ["From: " + username, "Subject: Test client using smtplib", "To: " + rcpt, "MIME-Version: 1.0", "Content-Type: text"]
messageHeader = "\r\n".join(messageHeader)
print('Initializing sendEmail sequence......')

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
connection.sendmail(username, rcpt, messageHeader + '\r\n' + msg)

# close connection
connection.quit()

#print email sent message
print('Email sent.')
