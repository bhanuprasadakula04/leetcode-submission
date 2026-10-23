class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        arr=[]
        seen=set(nums)
        for i in range(1,len(nums)+1):
            if i not in seen:
                arr.append(i)
        return arr