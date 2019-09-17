#规定其他模块from model03 import * 可以导入的内容
if __name__ == '__main__':
    print('模块1')
    print(__name__)
    #查看文档字符串
    print(__doc__)
    print(__file__)