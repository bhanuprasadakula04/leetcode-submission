class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen2={}
        seen1={}
        new=''
        for i in t:
            seen2[i]=seen2.get(i,0)+1
        for j in s:
            seen1[j]=seen1.get(j,0)+1
        for val,key in seen2.items():
            if seen2[val] > seen1.get(val, 0):
                return val
