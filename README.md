# Socket Netcat

<img src="res/cat.gif" alt="CAT" width="300px">

## Overview

`socket_netcat` is a Python script for basic network communication. It connects to a specified server, sends a message, and prints the server's response. This script is a simple implementation of the Unix utility `netcat`, often used for reading from and writing to network connections using TCP or UDP.

## Features

- Connect to a server using hostname and port.
- Send a specified message to the server.
- Receive and display the server's response.

## Requirements

- Python 3.6 or higher

## Usage

To use `socket_netcat`, simply run the script with Python. Specify a server to connect to and a message to sends as arguments.

```bash
python socket_netcat.py
```

## Configuration

You can modify the `hostname`, `port`, and `content` variables in the script to change the server you're connecting to, the port you're using, and the message you're sending, respectively.

## Example

```python
netcat(hostname="foo.bar", port=9000, content="Please respond!")
```

This will connect to `foo.bar` on port `9000` and send the message "Please respond!".

## License

This project is open source and available under the [MIT License](LICENSE).
