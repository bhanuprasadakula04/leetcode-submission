class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen=set()
       for i in range(len(nums)):
            complement=target-nums[i]
            if complement in seen:
                for j in range(i):
                    if nums[j]==complement:
                        return [j,i]
            seen.add(nums[i])

