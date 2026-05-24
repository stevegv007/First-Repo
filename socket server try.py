import socket
import variable

print('ill try sockets in this file')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 5555

sock.bind((HOST, PORT))

sock.listen()

print("server is listening...")

conn, addr = sock.accept()

print(f"Connected to {addr}")

while True:
    message = conn.recv(1024).decode()

    if not message:
        break

    print(f"Client: {message}")

    reply = input("You: ")

    conn.send(reply.encode())

conn.close()
sock.close()