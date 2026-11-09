class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        seen = {}

        for i, val in enumerate(list1):
            seen[val] = i

        min_sum = float('inf')
        ans = []

        for j, val in enumerate(list2):
            if val in seen:
                total = j + seen[val]

                if total < min_sum:
                    min_sum = total
                    ans = [val]

                elif total == min_sum:
                    ans.append(val)

        return ans