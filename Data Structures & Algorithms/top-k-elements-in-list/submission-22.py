from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        output = list(sorted(counter.items(), key=lambda item: item[1]))[-k:]
        return list(map(lambda item: item[0], output))
