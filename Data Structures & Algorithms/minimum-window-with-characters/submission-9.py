def areCountersEqual(s: dict, t: dict):
    for key, tValue in t.items():
        if tValue > s[key]:
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return t
        minLen = math.inf
        res = ""
        counterT = collections.Counter(t)
        counterS = defaultdict(int)
        for c in s[: len(t)]:
            counterS[c] += 1

        l, r = 0, len(t) - 1
        while r < len(s):
            windowSize = r - l + 1
            start, end = s[l], s[r]
            if areCountersEqual(counterS, counterT):
                print("found")
                if minLen > windowSize:  # if found a better solutiion
                    minLen = windowSize
                    res = s[l : r + 1]
                counterS[start] -= 1  # move left forward
                l += 1  # shrink
                if l > r:
                    r += 1
                    if r == len(s):
                        break
                    counterS[s[r]] += 1
            else:
                r += 1
                if r == len(s):
                    break
                counterS[s[r]] += 1
                if windowSize >= minLen:
                    l += 1
                    counterS[start] -= 1

            print()

        return res
