# 分解质因数,输入一个正整数,分解质因数，
#   如输入:90,则打印:
#      90 = 2 * 3 * 3 * 5
#     质因数是指最小能被原数整除的素数（不包括1)


def znum(num):
    n = 2
    while n <= num:
        if num % n == 0:
            num /= n
            print('质因数是%d'%n)
        else:
            n+=1

znum(90)

import select