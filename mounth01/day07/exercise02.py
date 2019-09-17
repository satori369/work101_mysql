s1 = {'曹操','刘备','孙权'}
s2 = {'曹操','刘备','关羽','张飞'}
print('是经理也是技术的有%s'%(s1&s2))
print('是经理不是技术的有%s'%(s1-s2))
print('不是经理,是技术的有%s'%(s2-s1))
print('张飞是经理么,%s'%('张飞' in s1))
print('总共有%s人'%(len(s2|s1)))
print('身兼一职的有%s人'%(len(s2^s1)))


dict_persons = {
    '经理':{'曹操','刘备','孙权'},
    '技术':{'曹操','刘备','关羽','张飞'}
}
print(dict_persons['经理'] & dict_persons['技术'])
print(dict_persons['经理'] - dict_persons['技术'])
print(dict_persons['技术'] - dict_persons['经理'])
print('张飞' in dict_persons['经理'])
print(len(dict_persons['技术'] | dict_persons['经理']))
print(len(dict_persons['技术'] ^ dict_persons['经理']))