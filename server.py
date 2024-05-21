import socket
import threading
import json
import argparse
import re

def read_config(config_file):
    """Reads the configuration file to get the host and port."""
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config['host'], config['port']

def bwt_transform(s):
    """Performs the Burrows-Wheeler Transform on the input string."""
    s = s + "$"
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    last_column = "".join(row[-1] for row in table)
    return last_column

def bwt_inverse(r):
    """Performs the inverse Burrows-Wheeler Transform to retrieve the original string."""
    if '$' not in r:
        return "Invalid BWT input: missing end-of-string marker ($)"
    
    n = len(r)
    table = [""] * n
    for i in range(n):
        table = sorted(r[j] + table[j] for j in range(n))
    s = [row for row in table if row.endswith("$")][0]
    return s.rstrip("$")

def handle_client(client_socket):
    """Handles client requests by performing the appropriate BWT operation."""
    try:
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")
        data = json.loads(request)
        
        if 'dna' in data:
            response = bwt_transform(data['dna'])
        elif 'bwt' in data:
            response = bwt_inverse(data['bwt'])
        else:
            response = "Invalid input"
        
        client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def start_server(host, port):
    """Starts the server to listen for client connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BWT Server")
    parser.add_argument('--config', type=str, required=True, help="Path to the configuration file")
    args = parser.parse_args()

    host, port = read_config(args.config)
    start_server(host, port)

