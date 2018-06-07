import socket

url=raw_input("URL of page:")

path=raw_input("enter the path:")

mysoc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysoc.connect((url,80))

mysoc.send('GET http://' + url +'\''+ path +' HTTP/1.0\n\n')

while True:

    data=mysoc.recv(512)

    if len(data) < 1:
        break

    print data

mysoc.close()
