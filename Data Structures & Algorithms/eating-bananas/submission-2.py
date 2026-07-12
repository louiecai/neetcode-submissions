class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)
        output = j

        while i <= j:
            k = (j + i) // 2
            localH = 0
            for pile in piles:
                localH += math.ceil(pile / k)
            
            if h < localH:
                # k has to be smaller than mid
                i = k + 1
            else:
                # k could be greater than mid
                output = min(output, k)
                j = k - 1
            
        
        return output
