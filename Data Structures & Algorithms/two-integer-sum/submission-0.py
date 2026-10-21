class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [min(seen[complement], i), max(seen[complement], i)]
            seen[nums[i]] = i