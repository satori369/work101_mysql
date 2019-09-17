word = input('单词:')
f = open('dict.txt','r')

for line in f:
    w = line.split(' ')[0]
    if w == word:
        print(line)
        break
    #遍历的单词已经大于目标,说明找不到了
    elif w > word:
        print('没找到')
        break
else:
    print('没找到')

f.close()

# print(data)


