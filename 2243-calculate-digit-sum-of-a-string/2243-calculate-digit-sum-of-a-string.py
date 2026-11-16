class Solution:
    def digitSum(self, s: str, k: int) -> str:
        res=""
        while len(s)>k:
            res=''
            for i in range(0,len(s),k):
                group=s[i:i+k]
                summ=0
                for ch in group:
                    summ+=int(ch)
                res+=str(summ)
            s=res
        return s