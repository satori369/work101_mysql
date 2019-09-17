#逆波兰表达式(dc)
from mounth02.day02.sstack import SStack

st=SStack()

# def dc(v1,v2,fh):
    # s1.push(v1)
    # s1.push(v2)
    # d2=s1.pop()
    # d1=s1.pop()
    # if fh=='+':
    #     s1.push(d2 + d1)
    #     return d2+d1
    # elif fh=='*':
    #     s1.push(d2 * d1)
    #     return d2*d1
    # elif fh=='-':
    #     s1.push(d2-d1)
    #     return d2-d1
    # elif fh=='/':
    #     s1.push(d2 / d1)
    #     return d2/d1

# print(dc(5,6,'+'))

while True:
    exp = str(input('逆波兰表达式'))
    tmp = exp.split(' ')
    for i in tmp:
        if i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == 'p':
            print(st.top())#看栈顶元素
        else:
            st.push(int(i))
    # s1.push(tmp)
    # v0=s1.pop()[0]
    # v1=s1.pop()[1]
    # v2=s1.pop()[2]
    # print(eval('%s%s%s'%(v0,v2,v1)))
    # print(s1.pop()[0])
# print(eval('%s%s%s'%('5','+','6')))
