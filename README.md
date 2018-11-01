# 세미나 때 마음껏 질문하세요!
### 앞에 강사가 이야기할때 질문하기 뻘쭘하셨죠?
### 설명 끝나면 내 머릿속의 질문이 사라져..
### 나만 모르는거면 어떡하지?

## 괜찮습니다! 옆 친구도 당연히 모르니 마음껏 질문하세요!

![client](../img/client.png)  
![server](../img/server.png)


아래의 코드를 Python IDLE에 넣고 실행합시다


```python
import socket
from threading import Thread
 
# 서버 IP 입력합시다
HOST = '여기에 제가 부르는 서버를 입력하세요'
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
            sock.send(msg.encode())
            break
 
         sock.send(msg.encode())
             
runChat()
```