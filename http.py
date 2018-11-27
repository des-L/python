from socket import *
from multiprocessing import Process

def fun(c_socket):
    re_data = c_socket.recv(1024)
    print("request data:",re_data)
        
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "Woooooooooo"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:",response)

    c_socket.send(bytes(response,"utf-8"))
    c_socket.close()
    
if __name__ == "__main__":
    s_socket = socket(AF_INET,SOCK_STREAM)
    s_socket.bind(("",7788))
    s_socket.listen(10)
    while True:
        c_socket,c_addr = s_socket.accept()
        print("(%s:%s)已连接"%c_addr)
        p = Process(target=fun,args=(c_socket,))
        p.start()
        c_socket.close()
