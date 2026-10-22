class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "[": "]", "{": "}"}
        for br in s:
            if br in mapping:
                stack.append(br)
            else:
                if not stack or br != mapping[stack.pop()]:
                    return False
        return not stack
        