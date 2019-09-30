from socket import *
import base64
import ssl
import getpass
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

image_data = open('happy.jpg', 'rb').read()
message = MIMEMultipart()


msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"

username = input('Username: ')
password = getpass.getpass('Password: ')
rcpt = input('receiver email: ')


# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = #Fill in start #Fill in end
mailserver = 'smtp-mail.outlook.com'
port = 587 #hotmail server port
# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024).decode() 
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
#Fill in end

# Send HELO command and print server response. 

heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

startTLS = "STARTTLS\r\n"
clientSocket.send(startTLS.encode())
receivedTLS = clientSocket.recv(1024).decode()
print("STARTTLS command response received: " + receivedTLS)

SSLClientSocket = ssl.wrap_socket(clientSocket)



userEncoding = (username).encode()
base64Encoding = base64.b64encode(userEncoding)

heloCommand = 'HELO Alice\r\n'

SSLClientSocket.send(heloCommand.encode())
recv1 = SSLClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


authenticationMessage = 'AUTH LOGIN\r\n'.encode()
SSLClientSocket.send(authenticationMessage)
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print("auth login: " + receivedAuthentication)
SSLClientSocket.send(base64Encoding + '\r\n'.encode())
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print('auth username: ' + receivedAuthentication)

passwordEncoding = (password).encode()
base64Encoding = base64.b64encode(passwordEncoding)

SSLClientSocket.send(base64Encoding + '\r\n'.encode())
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print('auth password: ' + receivedAuthentication)


# Send MAIL FROM command and print server response.
 
# Fill in start
mailFrom = 'MAIL FROM: ' + username + ' \r\n'
SSLClientSocket.send(mailFrom.encode())
received2 = SSLClientSocket.recv(1024).decode()
print('MAIL FROM command response received: ' + received2)

# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
rcptTo = 'RCPT TO: ' + rcpt + '\r\n'
SSLClientSocket.send(rcptTo.encode())
received3 = SSLClientSocket.recv(1024).decode()
print('RCPT TO command response received: ' + received3)

# Fill in end




# Send DATA command and print server response.

# Fill in start
data = "DATA\r\n"
SSLClientSocket.send(data.encode())
received4 = SSLClientSocket.recv(1024).decode()
print('DATA command response received: ' + received4) # pictures go here


# Fill in end




# Send message data.

# Fill in start
messageSubject = 'SUBJECT: Test to see if client works\r\n'
SSLClientSocket.send(messageSubject.encode())

text_MIME = MIMEText("hello world!\n")
message.attach(text_MIME)
image_MIME = MIMEImage(image_data, 'jpeg')
message.attach(image_MIME)
messageContent = message.as_string()
SSLClientSocket.send(messageContent.encode())


# messageContent = msg
# SSLClientSocket.send(messageContent.encode())


# Fill in end

# Message ends with a single period.

# Fill in start
SSLClientSocket.send(endmsg.encode())
# Fill in end




# Send QUIT command and get server response.

# Fill in start
quitCommand = 'QUIT\r\n'
SSLClientSocket.send(quitCommand.encode())
received5 = SSLClientSocket.recv(1024).decode()
print('QUIT command response received: ' + received5)
SSLClientSocket.close()
clientSocket.close()
# Fill in end



import smtplib

messageHeader = ["FROM: " + username, "Subject: Test client using smtplib", "TO: " + rcpt, "MIME-Version: 1.0", "Content-Type: text"]
messageHeader = "\r\n".join(messageHeader)
print('now sending email...')

connection = smtplib.SMTP(mailserver, port)
connection.ehlo()
connection.starttls()
connection.ehlo()
connection.login(username, password)
connection.sendmail(username, rcpt, messageHeader, messageHeader + '\r\n\r\n I love computer networks!')
connection.quit()

