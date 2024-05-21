import socket
import json
import argparse
import re

def send_request(host, port, data):
    """Sends a request to the server and prints the response."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(json.dumps(data).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(response)
    client.close()

def is_valid_dna(sequence):
    """Checks if the sequence is a valid DNA string."""
    return bool(re.match(r'^[ATCG]+$', sequence))

def is_valid_bwt(sequence):
    """Checks if the sequence is a valid BWT string."""
    return '$' in sequence

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BWT Client")
    parser.add_argument('host', type=str, help="Server host")
    parser.add_argument('port', type=int, help="Server port")
    parser.add_argument('query_type', type=str, choices=['dna', 'bwt'], help="Type of query: 'dna' or 'bwt'")
    parser.add_argument('sequence', type=str, help="DNA sequence or BWT (use \\$ to escape $)")

    args = parser.parse_args()

    if args.query_type == 'dna':
        if not is_valid_dna(args.sequence):
            print("Invalid DNA sequence. Only characters A, T, C, G are allowed.")
            exit(1)
        data = {'dna': args.sequence}
    elif args.query_type == 'bwt':
        if not is_valid_bwt(args.sequence):
            print("Invalid BWT input. Missing end-of-string marker ($).")
            exit(1)
        data = {'bwt': args.sequence}

    send_request(args.host, args.port, data)

