"""
with.py
with语句生成文件对象
"""

with open('4.txt') as f: # 以只读方式生成f对象
    data = f.read()
    print(data)

# with语句块结束,f会被自动清理
