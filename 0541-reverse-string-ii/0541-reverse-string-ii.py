class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)
        for i in range(0, len(res), 2*k):
            start = i
            end = min(i + k, len(res))
            res[start:end] = res[start:end][::-1]
        return "".join(res)