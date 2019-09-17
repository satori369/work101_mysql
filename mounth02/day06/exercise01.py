from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

def find_word(word):
    f = open('dict.txt', 'r')

    for line in f:
        w = line.split(' ')[0]
        if w == word:
            return line

        elif w > word:
            return '没找到'
    f.close()
    return '没找到'

server_addr = ('176.215.133.193',8889)
sockfd.bind(server_addr)

while True:
    word,addr = sockfd.recvfrom(1024)
    data = find_word(word.decode())
    sockfd.sendto(data.encode(),addr)