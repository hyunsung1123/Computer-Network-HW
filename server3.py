import socket 
      
LOCALHOST = "127.0.0.1"
PORT = 25002

server = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)
server.bind((LOCALHOST, PORT))

print("서버가 시작되었습니다.")
print("클라이언트의 요청을 기다리는 중입니다.")
msg = ''

while True:
    data,addr = server.recvfrom(1024)
    msg = data.decode()
    print("서버1로 부터 수식 "+msg+ " 을 전달받았습니다.")
    print("-------------------------------------------\n")

 
    if "*" in msg:
        operation_list = msg.split("*")
        result = int(operation_list[0])*int(operation_list[1])
    elif "/" in msg:
        operation_list = msg.split("/")
        result = int(operation_list[0])/int(operation_list[1])
    
    output = str(result)
    server.sendto(output.encode(),addr)
    print("서버1로 결과값 " + output + " 을 전달합니다.")
    print("-------------------------------------------\n")
