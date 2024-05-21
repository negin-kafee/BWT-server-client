#!/bin/bash

# Start the server in the background
python3 server.py --config config.json &
SERVER_PID=$!
sleep 2  # Wait for the server to start

# Test DNA to BWT
echo "Testing DNA to BWT"
python3 client.py 127.0.0.1 65433 dna AGCTTAGCTA

# Test BWT to DNA
echo "Testing BWT to DNA"
python3 client.py 127.0.0.1 65433 bwt ATT\$GGAACTC

# Test invalid BWT input
echo "Testing invalid BWT input"
python3 client.py 127.0.0.1 65433 bwt invalidbwt

# Run unit tests
echo "Running unit tests"
python3 -m unittest test_bwt.py

# Kill the server
kill $SERVER_PID

