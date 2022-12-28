
#서버1과 동일한 부분은 주석을 달지않았다.

import socket
 
LOCALHOST = "127.0.0.1"
PORT = 8080

#UDP 통신을 위한 소켓을 구성.
server = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)
server.bind((LOCALHOST, PORT))

print("서버가 시작되었습니다.")
print("클라이언트의 요청을 기다리는 중입니다.")
msg = ''
 
while True:
    data,addr= server.recvfrom(1024)
    msg = data.decode()
    print("서버1로 부터 수식 "+msg+ " 을 전달받았습니다.")
    print("-------------------------------------------\n")
    #문자열 수식을 띄어쓰기를 기준으로하여 나눠서 리스트에 저장한다.


    
    # 더하기 빼기 연산자에 맞춰 계산
    if "+" in msg:
        operation_list = msg.split("+")
        result = int(operation_list[0])+int(operation_list[1])
    elif "-" in msg:
        operation_list = msg.split("-")
        result = int(operation_list[0])-int(operation_list[1])
    
    #server1로 계산값을 전달한다.
    output = str(result)
    server.sendto(output.encode(),addr)
    print("서버1로 결과값 " + output + " 을 전달합니다.")
    print("-------------------------------------------\n")
