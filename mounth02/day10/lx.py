# 练习2,写一个程序，要求实现如下功能：
# (1). 创建一个文件student_info.txt
# (2). 在文件中写入如下两行内容：
# 	name:Bob  age:30  score: 90
	# name:Lucy age:25  score: 99

f = open('student_info.txt','a+')

d = {'name':None,'age':None,'score':None}

def huoqu():
    name = input('输入学生姓名')
    age= int(input('输入学生年龄'))
    score= int(input('输入学生成绩'))
    d['name']=name
    d['age']=age
    d['score']=score


def xieru(d):
    for item in d:
        c = '%s:%s    \n'% (item,d[item])
        f.write(c)

# 练习3：
# 写一个生成器函数myyield()，将练习2中student_info.txt中的两行内容生成一个生成器
# 然后用for语句打印这两行内容：

def myyield():
    fr = open('student_info.txt', 'r')
    frr=f.readlines()
    for i,c in enumerate(frr):
        print(c)
    fr.close()

if __name__ == '__main__':
    # huoqu()
    # xieru(d)
    myyield()


    f.close()
