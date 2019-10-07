from socket import *
import base64
import ssl
import getpass

#message to be sent
msg = '\r\nRuiqi Tian (rtian25) 250961103'
endmsg = "\r\n.\r\n"

#dynamic username, password and recipient input
username = 'richy990113@hotmail.com'
password = getpass.getpass('Password: ')
rcpt = 'manidimi123123@hotmail.com'


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

# Send STARTTLS command and print server response

startTLS = "STARTTLS\r\n"
clientSocket.send(startTLS.encode())
recvTLS = clientSocket.recv(1024).decode()
print("STARTTLS command response: " + recvTLS)

# wrap socket

SSLClientSocket = ssl.wrap_socket(clientSocket)


# encode username with base64 

userEncode = (username).encode()
userBase64Encode = base64.b64encode(userEncode)

# send HELO command again and print server response

heloCommand = 'HELO Alice\r\n'

SSLClientSocket.send(heloCommand.encode())
recv1 = SSLClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# send AUTH LOGIN command along with username

authMsg = 'AUTH LOGIN\r\n'.encode()
SSLClientSocket.send(authMsg)
recvAuth = SSLClientSocket.recv(1024).decode()
print("auth login: " + recvAuth)
SSLClientSocket.send(userBase64Encode + '\r\n'.encode())
recvAuth = SSLClientSocket.recv(1024).decode()
print('auth username: ' + recvAuth)

# encode password with base64

pwdEncode = (password).encode()
pwdBase64Encode = base64.b64encode(pwdEncode)

# send password and print server response

SSLClientSocket.send(pwdBase64Encode + '\r\n'.encode())
recvAuth = SSLClientSocket.recv(1024).decode()
print('auth password: ' + recvAuth)


# Send MAIL FROM command and print server response.
 
# Fill in start
mailFrom = 'MAIL FROM: ' + username + ' \r\n'
SSLClientSocket.send(mailFrom.encode())
recvMailFrom = SSLClientSocket.recv(1024).decode()
print('MAIL FROM command response received: ' + recvMailFrom)

# Fill in end



# Send RCPT TO command and print server response.

# Fill in start
rcptTo = 'RCPT TO: ' + rcpt + '\r\n'
SSLClientSocket.send(rcptTo.encode())
recvRcptTo = SSLClientSocket.recv(1024).decode()
print('RCPT TO command response received: ' + recvRcptTo)

# Fill in end



# Send DATA command and print server response.

# Fill in start
data = "DATA\r\n"
SSLClientSocket.send(data.encode())
recvData = SSLClientSocket.recv(1024).decode()
print('DATA command response received: ' + recvData) # pictures go here
# Fill in end



# Send message data.

# Fill in start
messageSubject = 'SUBJECT: Test to see if client works\r\n'
SSLClientSocket.send(messageSubject.encode())

messageContent = msg
SSLClientSocket.send(messageContent.encode())
# Fill in end



# Message ends with a single period.

# Fill in start
SSLClientSocket.send(endmsg.encode())
# Fill in end



# Send QUIT command and get server response.

# Fill in start
quitCommand = 'QUIT\r\n'
SSLClientSocket.send(quitCommand.encode())
recvQuit = SSLClientSocket.recv(1024).decode()
print('QUIT command response received: ' + recvQuit)
SSLClientSocket.close()
clientSocket.close()
# Fill in end

