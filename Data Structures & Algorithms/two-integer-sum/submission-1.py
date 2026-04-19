class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, value in enumerate(nums):
            diff = target - value
            if value in hash_map:
                return sorted([hash_map[value], i])
            hash_map[diff] = i