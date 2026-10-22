from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            
        return sorted(counts, key=counts.get, reverse=True)[:k]
        