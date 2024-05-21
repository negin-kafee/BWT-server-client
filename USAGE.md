# BWT Server and Client Usage

This document provides detailed examples and scenarios for using the BWT server and client.

## Starting the Server

Ensure the server is configured correctly in `config.json`:
```json
{
    "host": "127.0.0.1",
    "port": 65433
}

python3 server.py --config config.json

Running the Client

DNA to BWT
Convert a DNA sequence to its Burrows Wheeler Transform:
python3 client.py 127.0.0.1 65433 dna AGCTTAGCTA

Example output:
ATT$GGAACTC

BWT to DNA
Convert a Burrows Wheeler Transform back to the original DNA sequence. Note the use of escaping for the $ character:
python3 client.py 127.0.0.1 65433 bwt ATT\$GGAACTC

Example output:
AGCTTAGCTA


Error Handling

If you provide an invalid BWT (one that does not contain the $ character), the server will respond with an error message:

python3 client.py 127.0.0.1 65433 bwt invalidbwt

Example output:
Invalid BWT input: missing end-of-string marker ($)






