# class Solution:
#
#   def printListFromTailThHead(self,listNode):
#
#       result = []
#       while listNode:
#           result.insert(0,listNode.val)
#           listNode = listNode.next
#           return result
num = 1
#短路逻辑 逻辑运算时 如果前面的条件能判断出最终的结果
#后面的代码就不会执行
#尽量将复杂的判断放到后边
# and  发现第一个结果为false 就有结论了
#后续条件不再判断
# result = num == 1 and input('请输入a') == 'a'
#or 发现第一个结果为true
#后续条件不再判断
result1 = num + 1 or input('请输入a')  == 'a'





