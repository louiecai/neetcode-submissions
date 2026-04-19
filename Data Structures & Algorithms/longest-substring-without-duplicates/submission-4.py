class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {}
        seen[s[0]] = 0
        longest = 1
        l = 0

        for r, char in enumerate(s[1:]):
            r += 1
            if char in seen:
                l = max(seen[char] + 1, l)
            seen[char] = r
            longest = max(longest, r - l + 1)
            print(l, r)
        
        return longest