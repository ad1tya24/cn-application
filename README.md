# File Transfer Application
Computer Networks Project Application

> The project is not running using a concurrent server.

The application will allow for transfer of data:
- From the client to the server(server here will act like a file backup, can be external to the users folder)
- The current program can handle only 1 client at a time. First the first client is served then the next client will be served - **One at a Time**. To make this work with multiple clients at the same time we'll have to make a ***multi-threaded application using socket***.
- From the client to another client(client 1 will act as server and client 2 will act as receiver). To make this work we'll need to fix the issue with sending multiple files ***by creating another function that calls them and handles the closing of the sockets***.


---

## Languages

1. Python

## Libraries

1. socket


---

## Improvement Features

> Don't disclose this, these are our USPs.

- [ ] Encryption
- [ ] File Backup
