import socket

def scanning(port):
    target = "65.1.248.252"
    connect = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    connect.settimeout(1)
    reponse = connect.connect_ex((target,port))
    if reponse == 0:
        print(f"Port {port} is Open")
    else:
        print((f"Port {port} is Closed"))
    return

# for port_num in range(0, 5000):
#     scanning(port_num)

scanning(3001)