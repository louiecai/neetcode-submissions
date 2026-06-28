class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 1, len(height) - 2
        lMax, rMax = height[0], height[len(height) - 1]
        output = 0

        while l <= r:
            # min(lMax, rMax) - current
            print(l, r, lMax, rMax, output)
            if lMax < rMax:
                current = height[l]
                output += max(0, min(lMax, rMax) - current)
                lMax = max(lMax, current)
                l += 1
            else:
                current = height[r]
                output += max(0, min(lMax, rMax) - current)
                rMax = max(rMax, current)
                r -= 1
            
        
        return output
            
        