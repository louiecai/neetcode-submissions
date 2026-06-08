class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberMap = {} # num: index
        for i, num in enumerate(nums):
            if target - num in numberMap.keys():
                return list(sorted([i, numberMap[target - num]]))
            
            numberMap[num] = i
        
        return []