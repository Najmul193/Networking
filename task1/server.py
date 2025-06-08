import socket

port = 5660

format = "utf-8"

disconnect_msg = "End"

hostname = socket.gethostname()

host_addr = socket.gethostbyname(hostname)

server_socket_addr = (host_addr, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_socket_addr)

server.listen()

print("Server is listning.....")

while True:
    conn, addr = server.accept()
    print("Connected to ", addr)
    connected = True 

    while connected:
        initial = conn.recv(16).decode(format)
        print("Length of the msg to be send", initial)

        if initial:
            msg_length = int(initial)
            msg = conn.recv(msg_length).decode(format)

            if msg == disconnect_msg:
                print("Terminate connection with", addr)
                conn.send("Nice to meet you".encode(format))
                connected = False

            else:
                print(msg)
                conn.send("Recieved".encode(format))

    conn.close()
