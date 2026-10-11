class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr=[]
        val=0
        newnums2=set(nums2)
        for i in nums1:
            if i in newnums2:
                arr.append(i)
                newnums2.remove(i)
        return arr
        