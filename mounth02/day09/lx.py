nums = [2,7,11,15]
target= 9
class Solution(object):
    def twoSum(self,nums,target):
        d={}
        for i,num in enumerate(nums):
            if target - num in d:
                return [d[target - num],i]
            d[num] = i

s = Solution()
print(s.twoSum(nums,target))

for i,num in enumerate(nums):
    print(i,num)