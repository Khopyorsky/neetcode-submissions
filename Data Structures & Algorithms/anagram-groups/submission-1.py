class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result: defaultdict[str, list[str]] = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            result[key].append(s)

        return list(result.values())
        