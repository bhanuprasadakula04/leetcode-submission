class Solution:
    def secondHighest(self, s: str) -> int:
        letters=''
        digits=''
        for i in s:
            if i.isalpha():
                letters+=i
            else:
                digits+=i
        largest=float('-inf')
        seclarge=float('-inf')
        for i in digits:
            if int(i)>largest:
                seclarge=largest
                largest=int(i)
            elif int(i)>seclarge and int(i)!=largest:
                seclarge=int(i)
        if seclarge==float('-inf'):
            return -1
        return seclarge

            