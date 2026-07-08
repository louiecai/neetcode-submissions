class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i + 1 < j:
            mid = (i + j) // 2 
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                j = mid
            else:
                i = mid
        
        if target == nums[i]:
            return i
        if target == nums[j]:
            return j
        return -1
            