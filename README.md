# 세미나 때 마음껏 질문하세요!
### 앞에 강사가 이야기할때 질문하기 뻘쭘하셨죠?
### 설명 끝나면 내 머릿속의 질문이 사라져..
### 나만 모르는거면 어떡하지?

## 괜찮습니다! 옆 친구도 당연히 모르니 마음껏 질문하세요!

아래 예시 그림처럼 실행됩니다

#### 학생들의 실행창
![client](/img/client.png)  

#### 질문 후 서버의 실행창 
![server](/img/server.png)

### 작성자의 바램

**TCP/IP 통신**을 공부하면 아래의 내용이 재밌겠지만  
모르고 본다면 지옥입니다.  
한줄씩 코드 해석하기 보단   
일단 돌아가는 코드를 만지며 자신감을 쌓고 흥미를 붙여봅니다.  

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
            sock.send(msg.encode('utf-8'))
            break
 
         sock.send(msg.encode('utf-8'))
             
runChat()
```

#### 참고할 문서
* [맥 포트포워딩 하는 방법](https://superuser.com/questions/30917/how-to-make-a-port-forward-in-mac-os-x)
* [맥 포트포워딩 프로그램](https://www.codingmonkeys.de/portmap/)
* [원격에서 맥 접속하기](http://blog.arzz.com/446)
* [파이썬으로 채팅 서버 만들기](http://lidron.tistory.com/44)
* [파이썬으로 채팅 서버 만들기 2](http://qkqhxla1.tistory.com/189)
* [파이썬으로 채팅 서버 만들기 3](http://toyongyeon.cafe24.com/?p=517)