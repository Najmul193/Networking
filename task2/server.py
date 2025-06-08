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
print("Server is listening.....")

while True:
    conn, addr = server.accept()
    print("Connected to", addr)
    connected = True

    while connected:
        initial = conn.recv(16).decode(format)
        if initial:
            msg_length = int(initial.strip())
            msg = conn.recv(msg_length).decode(format)

            if msg == disconnect_msg:
                print("Terminate connection with", addr)
                conn.send("Terminating......".encode(format))
                connected = False
            else:
                vowels = 'aeiouAEIOU'
                vowel_count = 0

                for char in msg:
                    if char in vowels:
                        vowel_count+=1

                if vowel_count == 0:
                    response = "Not enough vowels"
                elif vowel_count <= 2:
                    response = "Enough vowels I guess"
                else:
                    response = "Too many vowels"

                conn.send(response.encode(format))

    conn.close()
