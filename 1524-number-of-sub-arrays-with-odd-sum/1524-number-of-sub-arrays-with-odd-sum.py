class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9+7
        even=1
        odd=0
        cnt=0
        value=0
        for i in arr:
            value=(value+i)%2
            if value==1:
                cnt+=even
                odd+=1
            else:
                cnt+=odd
                even+=1
            cnt%=mod

        return cnt            