class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        maxWindowLen = 1
        counter = defaultdict(int)
        counter[s[0]] += 1
        movedRight = len(s) >= 1

        while r <= len(s) - 1:
            print(s[l:r+1])
            if movedRight:
                counter[s[r]] += 1
            else:
                counter[s[l-1]] -= 1
                counter[s[r]] += 1
            print(counter)

            if r - l + 1 - max(counter.values()) <= k: # is a valid sequence
                maxWindowLen = max(maxWindowLen, r - l + 1)
                r += 1
                movedRight = True
            else:
                l += 1
                r += 1
                movedRight = False
            print('maxLen=' + str(maxWindowLen))
            print()
        
        print(counter)
        print(s[l:r+1])
        print('maxLen=' + str(maxWindowLen))
        return maxWindowLen