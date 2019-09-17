# 2.在控制台输入一个字符串 判断是否为回文
# 判断规则正向与反向相同
# 上海自来水来自海上
hw = (input('输入字符串'))
str1 = hw[0:len(hw):1]
str2 = hw[:-len(hw)-1:-1]
if (str1) == (str2):
    input('这是回文')
else:
    input('这不是回文')

