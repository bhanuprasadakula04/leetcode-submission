class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        summ=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (i-j+1)%2==1:
                    summ+=sum(arr[i:j+1])
        return summ