import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(f"Seu endereço IP: {IPAddr}")