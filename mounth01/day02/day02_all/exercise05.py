#练习
#古代称一斤16两  33两   2斤 1两
#在控制台获取两  input()
#计算 斤 和 两
#输出几斤几两    print()
#16:33~16:36
weight = int(input('请输入两：'))
jin = weight//16
liang = weight % 16
#2斤零1两
print(str(jin)+'斤零'+str(liang)+'两')