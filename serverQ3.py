import socket
import threading
import random

words = ["!false, it's funny because it's true", "Learning to code is useful no matter what your career ambitions are.", "Java is to Javascript what car is to carpet.", "copy-and-paste was programmed by programmers for programmers."]

def handle_client(client):
    while True:
        request = client.recv(1024).decode()
        if request == "SEND_WORD":
            word = random.choice(words)
            client.send(word.encode())
        else:
            client.send(b"INVALID_PROMPT")
            break
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.220.129", 8888))
server.listen(5)
print("Server is listening on 192.168.220.128:8888...")

while True:
    client, address = server.accept()
    print(f"Received connection from client...")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
