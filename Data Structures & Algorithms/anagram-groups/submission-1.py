from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {} # Counter: [strs...]
        for string in strs:
            counter = frozenset(Counter(string).items())
            print(counter)
            if counter in tracker:
                tracker[counter].append(string)
            else:
                tracker[counter] = [string]
        return list(tracker.values())
        