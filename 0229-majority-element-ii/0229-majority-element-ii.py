class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        seen={}
        arr=[]
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for val in seen:
            if seen[val]>len(nums)//3 :
                arr.append(val)
        return arr
                