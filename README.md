# BWT Server and Client

This project implements a server and a corresponding client to handle Burrows-Wheeler Transform (BWT) operations on DNA sequences.

## Overview

The server accepts a DNA sequence and returns its Burrows Wheeler Transform (BWT). It also accepts a BWT and returns the corresponding original DNA sequence.

## Features

- Efficiently handles client requests.
- Configurable host and port for the server.
- Client can contact the server with an arbitrary DNA or BWT query.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/negin-kafee/BWT-server-client.git

2. Navigate to the project directory:
    cd bwt_project

# Configuration

The server configuration is stored in a JSON file (config.json). You can specify the host and port in this file:


{
    "host": "127.0.0.1",
    "port": 65433
}



# Usage

Starting the Server
To start the server, run:

python3 server.py --config config.json

Running the Client
DNA to BWT

Convert a DNA sequence to its Burrows Wheeler Transform:
python3 client.py 127.0.0.1 65433 dna AGCTTAGCTA

Expected output:
ATT$GGAACTC

BWT to DNA

Convert a Burrows Wheeler Transform back to the original DNA sequence. Note the use of escaping for the $ character:
python3 client.py 127.0.0.1 65433 bwt ATT\$GGAACTC

Expected output:
AGCTTAGCTA



# Citations

This project was inspired by the following resources:

Ben Langmead: “Introduction to the Burrows-Wheeler Transform and FM Index”. Link: https://www.cs.jhu.edu/~langmea/resources/bwt_fm.pdf
Michael Burrows and David J Wheeler. “A block-sorting lossless data compression algorithm”. SRC research report, 1994. Link: https://www.cs.jhu.edu/~langmea/resources/burrows_wheeler.pdf





