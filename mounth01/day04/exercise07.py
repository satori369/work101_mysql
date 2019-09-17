#在控制台 获取一个字符串
#打印这个字符串的每一个字符的编码值
#字 -->数 ord('a')
#数 -->字 chr(97)

# num = input('输入字符')
# for i in num:
#   print(ord(i))

#2.在控制台 重复录入编码值 将编码值转为字符打印
# #如果录入的是空字符串 则退出程序
while True:
    str2 = input('输入编码值')
    if str2 == '':
        break
    print(chr(int(str2)))
