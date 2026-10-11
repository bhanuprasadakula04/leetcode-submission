class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n=int("".join(map(str,digits)))
        n+=1
        new=list(map(int,str(n)))
        return new
        