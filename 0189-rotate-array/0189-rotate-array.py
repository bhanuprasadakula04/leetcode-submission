class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums)==1 or len(nums)==0:
            return False
        k=k%len(nums)
        l=0
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l=0
        r=k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l=k
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        return nums