def normalize(d):
    return {k: v for k, v in d.items() if v != 0}

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Counter = defaultdict(int, collections.Counter(s1))
        s2Counter = defaultdict(int)

        l = 0
        for r, c in enumerate(s2):
            window = r - l + 1
            s2Counter[s2[r]] += 1
            if window < len(s1):
                continue
            
            if normalize(s1Counter) == normalize(s2Counter):
                return True
            
            # update s2counter
            s2Counter[s2[l]] -= 1
            l += 1
            
        return False


