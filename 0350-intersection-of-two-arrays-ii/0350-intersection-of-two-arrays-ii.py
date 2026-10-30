class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr=[]
        newnum=nums2
        for i in nums1:
            if i in newnum:
                arr.append(i)
                newnum.remove(i)
        return arr