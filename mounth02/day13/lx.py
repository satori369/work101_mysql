import re

a = '4g4z4g45tw@qq163.com'

c=re.findall('\w+@\w+\\.com',a)
print(c)

a='f451b8_f'
                          #团 组
c=re.findall('\w{8,12}',a)#.group()
print(c)

'so easy'
c = re.search(r'(王|李)\w{1,3}',"王者荣耀").group()
print(c)

# In [50]: re.findall('\[[-0-9]+\]',"[52],[6],[1],[5-9]")


# (ab){4}