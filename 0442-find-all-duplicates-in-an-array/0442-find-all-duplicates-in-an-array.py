class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen={}
        arr=[]
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for val in seen:
            if seen[val]>1:
                arr.append(val)
        return arr
