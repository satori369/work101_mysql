# list01=[]

# 去零
def quling():
    for i in range(len(list01)-1,-1,-1):
        if list01[i]==0:
            del list01[i]
            list01.append(0)


# 合并
def hebing():
    quling()
    for i in range(len(list01)-1):
        if list01[i]==list01[i+1]:
            list01[i]+=list01[i+1]
            del list01[i+1]
            list01.append(0)

game_map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
#zuoyi
def zuoyi():
    for i in game_map:
        global list01
        list01=i
        hebing()

# zuoyi()
# print(game_map)

#youyi
def youyi():
    for i in game_map:
        global list01
        list01 = i[::-1]
        hebing()
        i[::-1]= list01

# youyi()
# print(game_map)


#fanzhuan
def fanzhuan(list01):
    for i in range(len(list01)):
        for c in range(i+1,len(list01)):
            list01[i][c],list01[c][i]=list01[c][i],list01[i][c]



# shangyi
def shangyi():
    fanzhuan(game_map)
    zuoyi()
    fanzhuan(game_map)
    youyi()
    fanzhuan(game_map)

    fanzhuan(game_map)

def xiayi():
    fanzhuan(game_map)
    youyi()
    fanzhuan(game_map)

