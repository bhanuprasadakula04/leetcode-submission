class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        arr=[]
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0)+1
        for val in seen:
            newval=sorted(seen,key=seen.get,reverse=True)
            arr=newval[:k]
        return arr