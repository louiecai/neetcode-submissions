class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        output = 0

        while l < r:
            print(l, heights[l], r, heights[r])
            area = min(heights[l], heights[r]) * (r - l)
            output = max(output, area)

            if l + 1 == r:
                break
            
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return output
            