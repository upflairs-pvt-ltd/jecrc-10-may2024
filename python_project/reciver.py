import socket
import os  
S = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

os.makedirs("Data",exist_ok=True)
ip_address = "10.1.0.94"  
# ip_address = "127.0.0.1"
PORT_NO = 2525  # 0 -  65353 
complete_address = (ip_address,PORT_NO)
S.bind(complete_address)

print("hey i am recieving.....")
while True:
    data = S.recvfrom(100)
    message = data[0]
    ip_address =  data[1][0]
    decrypted_message  = message.decode('ascii')
    print(decrypted_message,"  >>>>>>  ",ip_address)


    with open(str(ip_address)+".txt",'a') as file: 
        file.write(decrypted_message)

    
     