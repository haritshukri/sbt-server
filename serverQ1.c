#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
	int sock, client_sock;
	struct sockaddr_in server, client;
    char message[5];
    int random_number;

    //create socket
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        printf("could not create socket");
    }

    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("192.168.220.129");
    server.sin_port = htons(8888);

    if (bind(sock, (struct sockaddr *) &server, sizeof(server)) < 0) {
        puts("bind failed");
        return 1;
    }

    listen(sock, 3);

    //connect to remote server
    puts("Waiting for incoming connections...");
    int c = sizeof(struct sockaddr_in);
    client_sock = accept(sock, (struct sockaddr *) &client, (socklen_t *) &c);
    if (client_sock < 0) {
        perror("connect error");
        return 1;
    }
    puts("Connected");

    //generate random number
    random_number = 100 + rand() % (999 - 100 + 1);
    sprintf(message, "%d", random_number);

    //send message
    send(client_sock, message, sizeof(message), 0);

    //close socket
    close(sock);

    return 0;
}
