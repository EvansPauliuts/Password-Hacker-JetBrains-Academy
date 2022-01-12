# Password-Hacker-JetBrains-Academy
This project jetbrains academy https://hyperskill.org/projects/80

## Work on project. Stage 1/5: Establishing a connection
### Objectives
Your program will receive command line arguments in this order:

1. IP address
2. port
3. message for sending 

The algorithm is the following:

1. Create a new socket.
2. Connect to a host and a port using the socket.
3. Send a message from the third command line argument to the host using the socket.
4. Receive the server’s response.
5. Print the server’s response.
6. Close the socket.

#### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

##### Example 1:

```shell
> python hack.py localhost 9090 password
Wrong password!
```

##### Example 2:

```shell
> python hack.py 127.0.0.1 9090 qwerty
Connection Success!
```