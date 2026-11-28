class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        new=''
        res=[]
        for i in words:
            if i=="".join(reversed(i)):
                return i 
        return new