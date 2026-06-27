class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        # prefix
        temp = 1
        for num in nums:
            output.append(temp)
            temp *= num
        
        # postfix
        temp = 1
        for i, num in reversed(list(enumerate(nums))):
            output[i] *= temp
            temp *= num
        
        return output