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

print("Server is listening...")

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
                    print("Terminating connection with", addr)
                    conn.send("Terminating...".encode(format))
                    connected = False
                else:
                    try:
                        hours = int(msg)
                        if hours <= 40:
                            salary = hours * 200
                        else:
                            salary = 8000 + (hours - 40) * 300

                        response = f"Calculated Salary: Tk {salary}"
                    except ValueError:
                        response = "Invalid input."

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
