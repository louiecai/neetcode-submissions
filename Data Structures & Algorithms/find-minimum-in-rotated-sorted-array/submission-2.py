class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 0 1 2 3 4 5
        # 3 4 5 0 1 2
        # i   m     j
        #     i m   j
        #     i j 

        i, j = 0, len(nums) - 1
        if nums[i] < nums[j]:
            return nums[i]
        while i < j - 1:
            m = (i + j) // 2
            # print(f'i={i},j={j},m={m}')
            if nums[m] > nums[i]:
                i = m
            else:
                j = m 
        
        return min(nums[i], nums[j])