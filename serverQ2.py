import socket

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    #create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 8889
    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Server is ready to receive')

    while True:
        #wait for a client to connect
        client_socket, client_address = server_socket.accept()
        print('Client connected:', client_address)

        #receive data from the client
        data = client_socket.recv(1024).decode()
        print('Received data:', data)

        #convert the temperature from Fahrenheit to Celsius
        celsius = fahrenheit_to_celsius(float(data))

        #send data to the client
        client_socket.send(str(celsius).encode())

        #close socket
        client_socket.close()

if __name__ == '__main__':
   main()
