class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        total = 0
        seen = {0: 1}

        for num in nums:
            total += num
            rem = total % k

            count += seen.get(rem, 0)
            seen[rem] = seen.get(rem, 0) + 1

        return count