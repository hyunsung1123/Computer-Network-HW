# 소켓을 사용하기 위해서는 socket을 import해야 한다.
import socket
# 로컬은 127.0.0.1의 ip로 접속한다.
SERVER = "127.0.0.1"
# port는 위 서버에서 설정한 9999로 접속을 한다.
PORT = 25001
# 소켓을 만든다.
client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
# connect함수로 접속을 한다.
client.connect((SERVER, PORT))
# 반복문을 통해 클라이언트 작업 반복
while True:
    #Input으로 문자열수식을 입력받아 
    inp = input("END를 입력하면 종료됩니다. "+ "\n" + "수식을 입력해주세요 : ")
    #inp값이 "END"이면 반복문을 종료하여 클라이언트와 서버와의 접속을 끊는다.
    if inp == "END":
        break
    #위에서 연결한 서버로 inp데이터를 전송한다.
    client.send(inp.encode())   
    #서버로 부터 데이터를 수신받는다.
    answer = client.recv(1024)
    #수신받은 데이터를 decode하여 출력 한다.
    print("-----------------------------------\n")
    print("입력받은 수식의 답은 : "+answer.decode())
    print("")
client.close()