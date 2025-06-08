import socket
import threading

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

def handle_client(conn, addr):
    print("Connected to", addr)
    connected = True

    while connected:
        try:
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
                    vowel_count = sum(1 for char in msg if char in vowels)

                    if vowel_count == 0:
                        response = "Not enough vowels"
                    elif vowel_count <= 2:
                        response = "Enough vowels I guess"
                    else:
                        response = "Too many vowels"

                    conn.send(response.encode(format))
        except:
            break

    conn.close()
    print("Connection closed with", addr)

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
