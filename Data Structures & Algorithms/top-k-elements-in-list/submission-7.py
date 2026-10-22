from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequences: defaultdict[int, int] = defaultdict(int)
        for num in nums:
            frequences[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequence in frequences.items():
            buckets[frequence].append(num)

        result = []
        for frequency in range(len(buckets) - 1, 0, -1):
            for num in buckets[frequency]:
                if k == 0:
                    return result
                result.append(num)
                k -= 1
        return result
        