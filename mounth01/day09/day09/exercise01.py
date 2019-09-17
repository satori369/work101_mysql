# list01 = [
#     [2,0,2,0],
#     [2,2,0,0],
#     [4,2,4,2],
#     [4,4,0,0]
# ]

#将列表中的0 放到列表末尾
#[0,4,0,0] -->[4,0,0,0]
#[0,0,2,0] -->[2,0,0,0]
#基础思路 14:14~14:19
#取出列表中非0的数字 放入新列表
#再判断原列表有多少0 添加进新列表
#list.count(0)
# def zero_to_end(list_target):
#     new_list = []
#     for item in list_target:
#         if item != 0:
#             new_list.append(item)
#     #[0,4,0,0]  -->[4]
#     #再判断原列表有多少0 添加进新列表
#     #list_target.count(0) = 3
#     for i in range(list_target.count(0)):
#         new_list.append(0)
#
#     return new_list
#
# print(zero_to_end([0,4,0,0]))


# def zero_to_end(list_target):
    #列表推导式
    # new_list = [item for item in list_target if item != 0]
    #重复的生成一个[0] 然后和新列表拼接
    #[0]的个数是目标列表中0的个数
    #[0]*3
    #[0, 0, 0]
    #[4]+[0]*3
    #[4, 0, 0, 0]
    # new_list += [0]*list_target.count(0)
    # return new_list

# print(zero_to_end([2,0,2,0]))

def zero_to_end(list_target):
    #删除0元素 再在列表后追加
    #del list[1]
    #list.remove(0)
    for item in list_target:
        if item == 0:
            list_target.remove(item)
            list_target.append(item)
#     #返回列表
#     return list_target
# print(zero_to_end([2,0,2,0]))


#0往后移
def zero_to_end():
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)

#合并
def merge():
    zero_to_end()
    for i in range(len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            #合并  将后面的元素累加到前面的元素上
            list_target[i]+=list_target[i+1]
            #删除后面的元素
            del list_target[i+1]
            #补零
            list_target.append(0)


game_map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
#左移
#将二维列表中的每一个列表取出 交给merge函数操作
def move_left():
    for line in game_map:
        global list_target
        list_target = line
        merge()
#右移
# [2,0,0,2]   [4,0,0,0]   [0,0,0,4]
# 原始列表    先反转        合并       反转
#  line    list_target list_target   line
#[4,4,2,2]  [2,2,4,4]  [4,8,0,0]   [0,0,8,4]
#[2,4,0,4]  [4,0,4,2]  [8,2,0,0]   [0,0,2,8]
#思想 将二维列表的每行(从右向左)交给merge操作
#从右向左接受数据
def move_right():
    for line in game_map:
        global list_target
        list_target = line[::-1]
        merge()
        line[::-1] = list_target
        # line = list_target[::-1]
move_right()
print(game_map)
#######################################
#上下移动

def square_matrix(list01):
    for c in range(1,len(list01)):  # 123
        for i in range(c,len(list01)):
            list01[i][c - 1], list01[c - 1][i] = list01[c - 1][i], list01[i][c - 1]

def move_up():
    square_matrix(game_map)
    move_left()
    square_matrix(game_map)

def move_down():
    square_matrix(game_map)
    move_right()
    square_matrix(game_map)

move_down()
print(game_map)
