from socket import *
import base64
import ssl
import getpass

#message to be sent
msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"

#dynamic username, password and recipient input
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

# Send STARTTLS command and print server response

startTLS = "STARTTLS\r\n"
clientSocket.send(startTLS.encode())
receivedTLS = clientSocket.recv(1024).decode()
print("STARTTLS command response received: " + receivedTLS)

# wrap socket

SSLClientSocket = ssl.wrap_socket(clientSocket)


# encode username with base64 

userEncoding = (username).encode()
base64Encoding = base64.b64encode(userEncoding)

# send HELO command again and print server response

heloCommand = 'HELO Alice\r\n'

SSLClientSocket.send(heloCommand.encode())
recv1 = SSLClientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# send AUTH LOGIN command along with username

authenticationMessage = 'AUTH LOGIN\r\n'.encode()
SSLClientSocket.send(authenticationMessage)
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print("auth login: " + receivedAuthentication)
SSLClientSocket.send(base64Encoding + '\r\n'.encode())
receivedAuthentication = SSLClientSocket.recv(1024).decode()
print('auth username: ' + receivedAuthentication)

# encode password with base64

passwordEncoding = (password).encode()
base64Encoding = base64.b64encode(passwordEncoding)

# send password and print server response

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
received5 = SSLClientSocket.recv(1024).decode()
print('QUIT command response received: ' + received5)
SSLClientSocket.close()
clientSocket.close()
# Fill in end

