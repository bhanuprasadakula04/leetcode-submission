class Solution:
    def frequencySort(self, s: str) -> str:
        seen={}
        newval=""
        for i in s:
            seen[i]=seen.get(i,0)+1
        for val in seen:
            newone=sorted(seen,key=seen.get,reverse=True)
        for i in newone:
            newval+=i*(seen[i])
        return newval