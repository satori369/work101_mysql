class GraphicIterator:
    def __init__(self,data):
        self.__target = data
        self.__indexs = -1

    def __next__(self):
        # 如果没有数据则抛出异常
        if self.__indexs >= len(self.__target)-1:
            raise StopIteration
        # 返回数据
        self.__indexs += 1
        return self.__target[self.__indexs]

class GraphicManager:
    def __init__(self):
        self.__graphic = []

    def add_graphic(self, str_skill):
        self.__graphic.append(str_skill)

    def __iter__(self):
        return GraphicIterator(self.__graphic)


manager = GraphicManager()
manager.add_graphic("圆形")
manager.add_graphic("矩形")
manager.add_graphic("三角形")

for item in manager:
     print(item)


iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

