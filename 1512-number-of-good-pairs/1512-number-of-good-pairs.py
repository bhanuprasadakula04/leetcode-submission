class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        cnt=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i<j:
                    cnt+=1
        return cnt