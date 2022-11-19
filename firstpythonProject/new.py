import socket
import sys
temp = input('Nhap dia chi IP vao de quet: ')
IP = socket.gethostbyname(temp)
print('Vui long doi, dang quet toi dia chi IP vua nhap', IP)
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP, port))
        if result == 0:
            print('Cong {}: dang mo'.format(port))
        sock.close()
except KeyboardInterrupt:
    print('Neu ban nhan Ctrl+C se thoat')
    sys.exit()
except socket.error:
    print('Khong ket noi duoc den may chu')
    sys.exit()