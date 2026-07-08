class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        queue = collections.deque([])
        for i, num in enumerate(nums):
            # insert new num
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            
            # pop old num
            while queue and queue[0] <= i - k:
                queue.popleft()

            # grab max
            if i + 1 < k:
                continue
            maxes.append(nums[queue[0]])

        return maxes
