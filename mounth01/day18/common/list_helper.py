'''
    定义项目中所有对容器的操作.
'''

class ListHelper:
    '''
        列表助手类
    '''
    @staticmethod#找生成器对象
    def find_all(iterable_target,func_condition):
        '''
            在可迭代对象中,查找满足条件的所有元素.
        :param iterable_target: 可迭代对象
        :param func_condition: 所有条件
        :return: 生成器对象
        '''
        for item in iterable_target:
            if func_condition(item):
                yield item
    ###########################
    @staticmethod#找单个元素
    def find_single(iterable_target,func_condition):
        '''
            在可迭代对象中,查找满足条件的所有元素.
        :param iterable_target: 可迭代对象
        :param func_condition: 所有条件
        :return: 元素
        '''
        for item in iterable_target:
            if func_condition(item):
                return item
###############################
    @staticmethod#元素总和
    def sum(iterable_target, func_condition):
        hduration = 0
        for item in iterable_target:
            hduration += func_condition(item)
        return hduration
###############################
    @staticmethod#找多个元素
    def select(iterable_target, func_condition):
        for item in iterable_target:
            yield func_condition(item)
###############################
    @staticmethod#查找最大值
    def get_max(iterable_target,func_condition):
        max = iterable_target[0]
        for i in range(1,len(iterable_target)):
            if func_condition(max) < func_condition(iterable_target[i]):
                max = iterable_target[i]
        return max
    @staticmethod  # 查找最小值
    def get_min(iterable_target, func_condition):
        max = iterable_target[0]
        for i in range(1, len(iterable_target)):
            if func_condition(max) > func_condition(iterable_target[i]):
                max = iterable_target[i]
        return max
###############################
    @staticmethod#升序
    def order_by(iterable_target,func_condition):
        for i in range(len(iterable_target)-1):
            for c in range(i+1,len(iterable_target)):
                if func_condition(iterable_target[i])>func_condition(iterable_target[c]):
                    iterable_target[i],iterable_target[c]=iterable_target[c],iterable_target[i]
###############################
    @staticmethod  # 降序
    def order_reverse_by(iterable_target, func_condition):
        for i in range(len(iterable_target) - 1):
            for c in range(i + 1, len(iterable_target)):
                if func_condition(iterable_target[i]) < func_condition(iterable_target[c]):
                    iterable_target[i], iterable_target[c] = iterable_target[c], iterable_target[i]
###############################
    @staticmethod  # del删除
    def delete_all(iterable_target,func_condition):
        count=0
        for i in range(len(iterable_target) - 1, -1, -1):
            if func_condition(iterable_target[i]):
             del iterable_target[i]
             count +=1
        return count