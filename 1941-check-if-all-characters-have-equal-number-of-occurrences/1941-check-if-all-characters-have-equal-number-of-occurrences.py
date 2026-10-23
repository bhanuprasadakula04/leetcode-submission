class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        seen={}
        for i in s:
            seen[i]=seen.get(i,0)+1
        if len(set(seen.values()))==1:
            return True
        else:
            return False