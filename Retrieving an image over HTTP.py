import socket , time

mysoc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysoc.connect(('www.py4inf.com',80))

mysoc.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count=0

pic=""

while True:

    data=mysoc.recv(5120)

    if len(data) < 1 :
        break

    time.sleep(0.25)

    count+=len(data)

    print len(data),count

    pic+=data

mysoc.close()

pos = pic.find("\r\n\r\n")

print 'Header length',pos

print pic[:pos]

pic = pic[pos+4:]

fhand = open("stuff.jpg","wb")

fhand.write(pic);

fhand.close()
