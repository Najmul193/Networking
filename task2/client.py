import socket

port = 5660
format = 'utf-8'
data = 16
disconnected_msg = "End"

hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)
server_socket_addr = (host_addr, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_addr)

def msg_send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length = str(msg_length).encode(format)
    msg_length += b" " * (data - len(msg_length))

    client.send(msg_length)
    client.send(message)

    print(client.recv(2048).decode(format))

msg = f"aeiousdsds"
msg_send(msg)

msg_send(disconnected_msg)
