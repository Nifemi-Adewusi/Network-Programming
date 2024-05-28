import socket
import calendar

def wkday(yr, mm, dd):
    re =''
    wkd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    r = calendar.weekday(yr, mm, dd)
    d = wkd[r]
    re = re + 'Weekday of birthday year ' + str(yr) + ' month ' + str(mm) + ' day ' + str(dd) + " is " + str(d)
    return re 

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Start Server")
port = 8000
ip_address = '127.0.0.1'
host = socket.gethostname()
ss.bind((host, port))
ss.listen(5)
con, add = ss.accept()
print("address connected client {0} and port number {1}".format(add[0], add[1]))
data = con.recv(1024)
print("Message From Client Before Decoding", data)
data = data.decode()
print("Message From Client After Decoding", data)

msg = input("message to client: ")
con.sendall(bytes(msg.encode("ascii")))

data = con.recv(1024)
print("message birthday from client before decoding: ", data)
data = data.decode()
print("message birthday from client after decoding", data)

data = data.split()
print("Message after spilling:", data)

yr = data[0]
mm = data[1]
dd = data[2]

yr = int(yr)
mm = int(mm)
dd = -int(dd)



res = wkday(yr, mm, dd)
con.sendall(bytes(res.encode("ascii")))