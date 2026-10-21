class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for l in s:
            counts[l] = counts.get(l, 0) + 1
        for l in t:
            if l not in counts or counts[l] == 0:
                return False
            
            counts[l] -= 1

        return True
        