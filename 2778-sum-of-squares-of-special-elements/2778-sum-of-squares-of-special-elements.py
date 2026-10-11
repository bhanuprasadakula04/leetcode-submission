class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        summ=0
        for i in range(n):
            if n%(i+1)==0:
                product=nums[i]*nums[i]
                summ+=product
        return summ
        