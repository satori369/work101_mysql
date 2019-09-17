

def jzzz(list):
    '''

    :param list02:
    :return:
    '''
    list02=[]
    for c in range(len(list[0])):
        list02.append([])
        for i in range(len(list)):
            list02[c].append(list[i][c])

    return list02
    # print(list02)
list01 = [
     [0,1,2,3,4],
     [1,28,45,6,7],
     [20,7,3,65,2],
    [4,5,6,7,8]
]
print(jzzz(list01))


