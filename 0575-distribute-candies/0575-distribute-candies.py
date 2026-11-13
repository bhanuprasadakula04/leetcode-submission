class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n=len(candyType)
        val= len(set(candyType))
        return min(val,n//2)