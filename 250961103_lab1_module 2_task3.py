from socket import *
import base64
import ssl
import getpass

msg = '\r\nRuiqi Tian (rtian25) 250961103'
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
print("STARTTLS command response: " + recvTLS)

SSLClientSocket = ssl.wrap_socket(clientSocket)

userEncode = (username).encode()
userBase64Encode = base64.b64encode(userEncode)

heloCommand = 'HELO Alice\r\n'

SSLClientSocket.send(heloCommand.encode())
recv1 = SSLClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

authMsg = 'AUTH LOGIN\r\n'.encode()
SSLClientSocket.send(authMsg)
recvAuth = SSLClientSocket.recv(1024).decode()
print("auth login: " + recvAuth)
SSLClientSocket.send(userBase64Encode + '\r\n'.encode())
recvAuth = SSLClientSocket.recv(1024).decode()
print('auth username: ' + recvAuth)

pwdEncode = (password).encode()
pwdBase64Encode = base64.b64encode(pwdEncode)

SSLClientSocket.send(pwdBase64Encode + '\r\n'.encode())
recvAuth = SSLClientSocket.recv(1024).decode()
print('auth password: ' + recvAuth)

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

messageSubject = 'SUBJECT: Test to see if client works\r\n'
SSLClientSocket.send(messageSubject.encode())

messageContent = msg
SSLClientSocket.send(messageContent.encode())

SSLClientSocket.send(endmsg.encode())

quitCommand = 'QUIT\r\n'
SSLClientSocket.send(quitCommand.encode())
recvQuit = SSLClientSocket.recv(1024).decode()
print('QUIT command response received: ' + recvQuit)
SSLClientSocket.close()
clientSocket.close()
