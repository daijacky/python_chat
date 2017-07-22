# coding:utf-8
 
#  __author__ = 'Mark sinoberg'
#  __date__ = '2016/7/7'
#  __Desc__ = 创建一个简单的套接字监听请求
 
import socket, select
def broadcast_data (sock, message):
#Do not send the message to master socket and the client who has send us the message
    for socket in conn_list:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                conn_list.remove(socket)
if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 9998
     
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((HOST,PORT))
    print u'套接字已启动！'
    conn_list = []
    conn_list.append(s)
    while True:
        read_sockets,write_sockets,error_sockets = select.select(conn_list,[],[])
        for sock in read_sockets:
            # 发送到服务器请求
            if sock == s:
                    # Handle the case in which there is a new connection recieved through server_socket
                    data, addr = s.accept()
                    conn_list.append(data)
                    print 'Connected with ' + addr[0] + ':' + str(addr[1]),str(' : ')+data
                     
                    broadcast_data(data, "[%s:%s] entered room\n" % addr)
                 
            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data, addr = sock.recv(1024)
                    print 'Connected with ' + addr[0] + ':' + str(addr[1]),str(' : ')+data
                    broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                 
                 
                except:
                    sock.close()
                    conn_list.remove(sock)
                    continue