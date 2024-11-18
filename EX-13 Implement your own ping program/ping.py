from socket import *
from time import time
import sys

def ping_server(host='127.0.0.1', port=12345):
    with socket(AF_INET, SOCK_DGRAM) as s:
        try:
            s.settimeout(2)
            start = time()
            s.sendto(b'ping', (host, port))
            data, addr = s.recvfrom(1024)
            end = time()
            print(f"Received {data.decode()} from {addr} in {end - start:.2f} seconds")
        except timeout:
            print("Request timed out")
        except ConnectionResetError:
            print("Request timed out")


host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
ping_server(host)
