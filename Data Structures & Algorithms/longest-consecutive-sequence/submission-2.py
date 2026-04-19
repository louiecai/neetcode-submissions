class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        buckets = defaultdict(lambda: False)
        conseq = 0
        max_conseq = 0

        for num in nums:
            buckets[num] = True

        for num in range(min(nums), max(nums) + 1):
            if not buckets[num]:
                conseq = 0
            else:
                conseq += 1
            max_conseq = max(max_conseq, conseq)
        
        return max_conseq
