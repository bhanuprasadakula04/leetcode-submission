class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        seen = {}
        seen2 = {}
        arr = []

        if len(p) > len(s):
            return arr

        for i in p:
            seen[i] = seen.get(i, 0) + 1

        l = 0

        for r in range(len(s)):
            seen2[s[r]] = seen2.get(s[r], 0) + 1

            if r - l + 1 > len(p):
                seen2[s[l]] -= 1

                if seen2[s[l]] == 0:
                    del seen2[s[l]]

                l += 1

            if seen == seen2:
                arr.append(l)

        return arr