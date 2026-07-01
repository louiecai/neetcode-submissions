class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = {} # letter: index
        maxLen = 0
        start = 0
        for i, c in enumerate(s):
            if c in current and current[c] >= start:
                start = current[c] + 1
            current[c] = i
            maxLen = max(maxLen, i - start + 1)

        return maxLen
