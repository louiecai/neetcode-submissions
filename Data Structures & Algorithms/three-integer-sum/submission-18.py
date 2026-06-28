class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            target = -num

            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[l] + nums[r]
                if temp == target:
                    output.append([num, nums[l], nums[r]]) 
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif temp < target:
                    l += 1
                elif temp > target:
                    r -= 1

        return output
