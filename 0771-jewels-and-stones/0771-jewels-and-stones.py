class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen1={}
        seen2={}
        cnt=0
        for i in jewels:
            seen1[i]=seen1.get(i,0)+1
        for i in stones:
            seen2[i]=seen2.get(i,0)+1
        for val in seen1:
            newval=val
            if newval in seen2:
                cnt+=seen2[val]
        return cnt