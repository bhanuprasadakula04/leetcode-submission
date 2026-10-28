class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        seen={}
        for i in range(len(pattern)):
            ch=pattern[i]
            word=words[i]
            if ch in seen:
                if seen[ch] != word:
                    return False
            else:
                if word in seen.values():
                    return False
                seen[ch] = word

        return True