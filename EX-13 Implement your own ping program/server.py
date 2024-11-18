import socket
def start_server(host='127.0.0.1',port=12345):
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
        s.bind((host,port))
        print(f"UDP server running on {host}:{port}")
        while True:
            data,addr=s.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
            s.sendto(b'ping',addr)
start_server()
