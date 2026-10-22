class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        result = []
        pos = 0
        while pos < len(s):
            hash_position = s.find("#", pos)
            word_length = int(s[pos: hash_position])
            
            start = hash_position + 1
            end = hash_position + 1 + word_length
            
            result.append(s[start: end])
            
            pos = end

        return result