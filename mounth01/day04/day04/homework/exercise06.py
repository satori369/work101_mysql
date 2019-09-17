#1.在控制台 获取一个字符串
#打印这个字符串的每一个字符的编码值
#字 --> 数 ord('a')
#数 --> 字 chr(97)
str1 = input('请输入文字:')
for ch in str1:
    print(ord(ch))
#2.在在控制台 重复录入编码值 将编码值转为字符打印
#如果录入的是空字符串 则退出程序
#休息+练习16:00~16:20
while True:
    str2 = input('请输入编码值')
    if str2 == '':
        break
    code_value = int(str2)
    print(chr(code_value))
    # print(chr(int(str2)))
