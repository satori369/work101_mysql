#定义在终端打印矩形的函数
#要求函数调用者提供行数 列数 和填充字符
#如 3 3 *
def juxing(int01,int02,char):
    # int01 = int(input('输入行'))
    # int02 = int(input('输入列'))
    # char= (input('输入填充字符'))
    for i in range(int01):
        for ii in range(int02):
            print(char,end=' ')
        print()


juxing(6,3,5)
# def print_rect(row,col,char):
#     for i in range(row):
#         for ii in range(col):
#             print(char,end=' ')
#         print()
#
# print_rect(3,5,'8')
# print_rect(3,5,'8')
# print_rect(3,5,'8')
# print_rect(3,5,'8')