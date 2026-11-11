class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr1=[]
        arr2=[]
        arr3=[]
        prefix=1
        suffix=1
        n=len(nums)
        ans=[1]*n
        for i in range(n):
            arr1.append(prefix)
            prefix*=nums[i]
        for j in range(n-1,-1,-1):
            arr2.append(suffix)
            suffix*=nums[j]
        arr2.reverse()
        for k in range(n):
            arr3.append(arr1[k]*arr2[k])
        return arr3