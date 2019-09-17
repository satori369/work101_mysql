from multiprocessing import Process,Pool,Queue
import os

q = Queue() # 消息队列

#拷贝文件
def copy_file(file,old_dir,new_dir):
    fr = open(old_dir+file,'rb')
    fw = open(new_dir+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data) #写入的字节数
        q.put(n)
# 创建进程池
def main():
    path = '/home/tarena/aid1907/mounth02/day09/'
    dir = input('输入要拷贝的文件目录:')
    old_dir = path + dir + '/' #原目录绝对路径
    new_dir = path + dir+'-备份/'
    os.mkdir(new_dir)
    file_list = os.listdir(old_dir)

    total_size = 0
    for file in file_list:
        total_size += os.path.getsize(old_dir+file)

    print('总共大小:%d M'%(total_size/1024//1024))

    pool = Pool(4)
    for file in file_list:
        pool.apply_async(copy_file,args=(file,old_dir,new_dir))
    pool.close()

    copy_size = 0 # 已经拷贝的大小
    while copy_size < total_size:
        copy_size += q.get() # 获取队列数量值
        print('拷贝了%.1f%%' % (copy_size/total_size*100))

    pool.join()

#关闭进程池


#回收进程池
if __name__ == '__main__':
    main()