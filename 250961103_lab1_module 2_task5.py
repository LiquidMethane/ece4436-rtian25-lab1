from socket import *
import base64
import ssl
import getpass
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

image_data = open('wat.jpg', 'rb').read()
message = MIMEMultipart()

msg = "\r\nRuiqi Tian (rtian25) 250961103" 
endmsg = "\r\n.\r\n"

username = 'richy990113@hotmail.com'
password = getpass.getpass('Password: ')
rcpt = 'manidimi123123@hotmail.com'

mailserver = 'smtp-mail.outlook.com'
port = 587 

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024).decode() 
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

startTLS = "STARTTLS\r\n"
clientSocket.send(startTLS.encode())
recvTLS = clientSocket.recv(1024).decode()
print("STARTTLS command response received: " + recvTLS)

SSLClientSocket = ssl.wrap_socket(clientSocket)

userEncode = (username).encode()
userB64encode = base64.b64encode(userEncode)

heloCommand = 'HELO Alice\r\n'

SSLClientSocket.send(heloCommand.encode())
recv1 = SSLClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

authMsg = 'AUTH LOGIN\r\n'.encode()
SSLClientSocket.send(authMsg)
recvAuthMsg = SSLClientSocket.recv(1024).decode()
print("auth login: " + recvAuthMsg)
SSLClientSocket.send(userB64encode + '\r\n'.encode())
recvAuthMsg = SSLClientSocket.recv(1024).decode()
print('auth username: ' + recvAuthMsg)

passwordEncoding = (password).encode()
base64Encoding = base64.b64encode(passwordEncoding)

SSLClientSocket.send(base64Encoding + '\r\n'.encode())
recvAuthMsg = SSLClientSocket.recv(1024).decode()
print('auth password: ' + recvAuthMsg)

mailFrom = 'MAIL FROM: ' + username + ' \r\n'
SSLClientSocket.send(mailFrom.encode())
recvMailFrom = SSLClientSocket.recv(1024).decode()
print('MAIL FROM command response received: ' + recvMailFrom)

rcptTo = 'RCPT TO: ' + rcpt + '\r\n'
SSLClientSocket.send(rcptTo.encode())
recvRcptTo = SSLClientSocket.recv(1024).decode()
print('RCPT TO command response received: ' + recvRcptTo)

data = "DATA\r\n"
SSLClientSocket.send(data.encode())
recvData = SSLClientSocket.recv(1024).decode()
print('DATA command response received: ' + recvData) 

messageSubject = 'SUBJECT: Test to see if client works with image\r\n'
SSLClientSocket.send(messageSubject.encode())

text_MIME = MIMEText("I love computer networks!\n")
message.attach(text_MIME)
image_MIME = MIMEImage(image_data, 'jpeg')
message.attach(image_MIME)
messageContent = message.as_string()
SSLClientSocket.send(messageContent.encode())

SSLClientSocket.send(endmsg.encode())

quitCommand = 'QUIT\r\n'
SSLClientSocket.send(quitCommand.encode())
recvQuit = SSLClientSocket.recv(1024).decode()
print('QUIT command response received: ' + recvQuit)
SSLClientSocket.close()
clientSocket.close()
