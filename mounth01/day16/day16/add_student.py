#!/usr/bin/env python3
import sys

#python的位置参数列表
print(sys.argv)
def add_student(name,id):
    print('添加学生成功，%s:%s' % (id,name) )

if __name__ == "__main__":
    add_student(sys.argv[1],sys.argv[2])