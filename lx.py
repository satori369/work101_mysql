class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            if array==[[]]:
                print('列表为空')
                return
            if target < array[i][0]:
                continue
            for c in range(len(array[0])):
                if target == array[i][c]:
                    return True
        return False
#
s=Solution().Find(16,[[]])
print(s)

# a=[[]]
# print(a)

# print(a[0][0])

# s='1 J2 W2017-01# 123 1234 2008-10-01 2008-11-01'
# f='1 J2'
# # l=('a',1,'b',2)
# #
# # print(len(l)*'%s')
# #
# # ldse=len(l) * '%s'
# # msg='%s'%ldse
# # print(msg)
#
# # s.split()
# # print(f.split())
# # fs=f.split()
# # yz=()
# # for i in fs:
# #     yz+=i
# # print(yz)
# # print('id:%s \n车型:%s'%f.split())
#
# a=('bus2',)
# b=('name','def')
# b=a+b
#
# sql = "insert into %s (chexfayundate,tel)values ('%s','%s')"%b
#
# print(sql)
#
#



