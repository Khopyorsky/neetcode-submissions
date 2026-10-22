from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        return sorted(counts, key=lambda x: counts[x], reverse=True)[:k]

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        frequences: defaultdict[int, int] = defaultdict(int)
        result = []
        for i in range(len(nums), 1, -1):
            if frequences[i] > 0:
                result.append(frequences[i])
                k -= 1
            if k == 0:
                break
        return result
        