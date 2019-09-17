#定义函数 在控制台接受用户输入的成绩
#如果出现异常 就继续输入 直到正确位置

def chengji():
    while True:
        try:
            score=int(input('输入成绩'))
            return score
        except:
            print('输入有误')





if __name__ == '__main__':
            print(chengji())
#
#             print('请输入整数')
#         except KeyboardInterrupt:
#             print('\n用户中断输入')
#


