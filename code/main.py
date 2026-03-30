import socket
ip = "192.168.1.8"
def check_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        request = "GET / HTTP/1.1\r\nHost: " + ip + "\r\n\r\n"
        s.send(request.encode())
        response = s.recv(4096)
        print(response.decode(errors="ignore"))
        s.close()
        return True
    except:
        return False

check_port(ip, 80)