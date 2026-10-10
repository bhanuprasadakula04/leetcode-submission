class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        largest=0
        seclargest=0
        for i in range(len(nums)):
            if nums[i]>=largest:
                seclargest=largest
                largest=nums[i]
            elif nums[i]>seclargest and nums[i]!=largest:
                seclargest=nums[i]
        return (largest-1)*(seclargest-1)
            
            

                
