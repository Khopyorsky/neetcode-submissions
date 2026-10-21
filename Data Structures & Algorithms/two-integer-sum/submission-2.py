class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_modified: list[tuple[int, int]] = sorted(
            [(i, nums[i]) for i in range(len(nums))],
            key=lambda x: x[1],
        )
        i = 0
        j = len(nums_modified) - 1
        while i < j:
            if nums_modified[i][1] + nums_modified[j][1] == target:
                return [min(nums_modified[i][0], nums_modified[j][0]), max(nums_modified[i][0], nums_modified[j][0])]
            if nums_modified[i][1] + nums_modified[j][1] > target:
                j -= 1
            else:
                i += 1

        return []