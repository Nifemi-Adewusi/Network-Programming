# print("Hello World")
import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Start Client:")
port = 8000
ip_address = '127.0.0.1'
host = socket.gethostname()
# cs.bind((host, port))

cs.connect((host, port))
msg = input("Message to server: ")
cs.sendall(bytes(msg.encode("ascii")))

data = cs.recv(1024).decode()
print("message from server", data)

msg = input("message birthday, year/ month/ day")
cs.sendall(bytes(msg.encode("ascii")))

data = cs.recv(1024).decode()

print("My Request From Server: ", data)
cs.close()