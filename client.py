import socket
from threading import Thread

# server.py가 돌아가는 컴퓨터가 서버입니다
# 서버 IP 입력합시다
HOST = '211.194.234.12'
PORT = 9009
 
def rcvMsg(sock):
   while True:
      try:
         data = sock.recv(1024)
         if not data:
            break
         print(data.decode())
      except:
         pass
 
def runChat():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      t = Thread(target=rcvMsg, args=(sock,))
      t.daemon = True
      t.start()
 
      while True:
         msg = input()
         if msg == '/quit':
            sock.send(msg.encode('utf-8'))
            break
 
         sock.send(msg.encode('utf-8'))
             
runChat()
