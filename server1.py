# 소켓을 사용하기 위해서는 socket을 import해야 한다.
import socket
# 로컬은 127.0.0.1의 ip로 접속한다.
LOCALHOST = "127.0.0.1"
PORT = 25001 # 최상단 클라이언트와의 포트 번호
PORT1 = 8080  # 더하기 빼기 서버와의 포트 번호
PORT2 = 25002 # 곱하기 나누기 서버와의 포트 번호
# TCP소켓을 만든다. server 소켓은 client와 연결하는 소켓이다.
server = socket.socket(socket.AF_INET,
                        socket.SOCK_STREAM)                      
# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
server.bind((LOCALHOST, PORT))
# 서버가 클라이언트의 접속을 허용하도록 합니다. 
server.listen(1)
print("서버가 시작되었습니다.")
print("클라이언트의 요청을 기다리는 중입니다.")
print("-------------------------------------------\n")
# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.   그럼 client 소켓과 addr(주소)를 튜플로 받는다.
clientConnection, clientAddress = server.accept()
#클라이언트와 연결되면 접속 주소가 출력된다.
print("Connected client :", clientAddress)
#클라이언트가 보낸 데이터를 담을 msg변수이다.
msg = ''
# 무한루프를 돌면서 
while True:
     # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다. 
    data = clientConnection.recv(1024)
    msg = data.decode()
    # END를 수신하면 루프를 중지합니다. 
    if msg == 'END':
        print("클라이언트하고의 연결이 끊겼습니다.")
        break
    print("클라이언트로 부터 수식 "+msg+" 을 입력받았습니다.")
        # operation이 +/- 면 server2 즉 8080포트인 clinet와 연결 후 데이터를 전송하고
        # *또는/면 server3즉 port번호가 25002인 client2와 연결 후 데이터를 전송합니다.
    if  "+" in msg or "-" in msg:
        #server2와 연결할 UDP소켓1 생성
        UDPclient = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)  
        print("더하기 빼기 서버로 식을 전달합니다.")
        print("-------------------------------------------\n")
        #수식을 전달합니다.
        UDPclient.sendto(msg.encode(),(LOCALHOST,PORT1))
        #수식의 결과값을 수신합니다.
        answer,add = UDPclient.recvfrom(1023)
        answer=answer.decode()
        print("서버로 부터 결과 값인 "+answer+" 을 받았습니다.")
        print("-------------------------------------------\n")
    elif "*" in msg or "/" in msg:
        #server2와 연결할 UDP소켓2 생성
        UDPclient2 = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)   
        print("곱하기/나누기 서버로 식을 전달합니다.")
        print("-------------------------------------------\n")
        #수식을 전달합니다.
        UDPclient2.sendto(msg.encode(),(LOCALHOST,PORT2))
        #수식의 결과값을 수신합니다.
        answer,add = UDPclient2.recvfrom(1023)
        answer = answer.decode()
        print("서버로 부터 결과 값인 "+answer +" 을 받았습니다.")
        print("-------------------------------------------\n")
    output = str(answer)
    clientConnection.send(output.encode())
    print("수식의 결과값인 "+output+" 을 클라이언트에게 전달합니다.")
    print("-------------------------------------------\n")
clientConnection.close()