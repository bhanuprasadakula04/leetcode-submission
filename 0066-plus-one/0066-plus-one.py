class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num=0
        for val in digits:
            num=num*10+val
        num+=1
        newnum=list(map(int,str(num)))
        return newnum