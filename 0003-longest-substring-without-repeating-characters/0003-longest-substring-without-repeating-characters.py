class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashval = set()
        left = 0
        max_len=0
        for right in range(len(s)):
            while s[right] in hashval:
                hashval.remove(s[left])
                left += 1
            hashval.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
