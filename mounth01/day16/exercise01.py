#定义一个函数 根据年月日计算星期
import time

# time_tuple=time.localtime()
def jsxqj(year,month,day):
    time_tuple=time.strptime('%d/%d/%d'%(year,month,day),'%Y/%m/%d')
    week_tuple=('星期一','星期二','星期三','星期四','星期五','星期六','星期日',)
    return week_tuple[time_tuple[6]]

# print(time.strptime("93/03/24 ",'%y/%m/%d '))

def life_days(birthday):
    time_tuple = time.strptime(birthday,"%Y/%m/%d")
    #生活的总秒数 = 当前时间戳 -出生的时间戳
    life_second =time.time() - time.mktime(time_tuple)
    return life_second/60/60//24




if __name__=='__main__':
    print(jsxqj(2019,8,21))
    print(life_days('1993/03/24'))
    



