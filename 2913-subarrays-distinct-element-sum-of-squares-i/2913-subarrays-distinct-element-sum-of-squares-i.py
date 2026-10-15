class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            seen=set()
            for j in range(i,len(nums)):
                seen.add(nums[j])
                cnt=len(seen)
                ans+=cnt*cnt
        return ans