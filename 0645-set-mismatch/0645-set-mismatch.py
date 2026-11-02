class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        arr=[]
        for index,value in enumerate(nums,start=1):
            if value in nums[index:]:
                dup=value
        for i in range(1,len(nums)+1):
            if i not in nums:
                miss=i
        arr.extend([dup,miss])
        return arr