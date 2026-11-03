class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for val in seen:
            if seen[val]>1:
                return val