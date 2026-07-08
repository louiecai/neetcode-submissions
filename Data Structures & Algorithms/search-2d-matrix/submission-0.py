def coordToIndex(row: int, col: int, n: int) -> int:
    return row * n + col

def indexToCoord(index: int, n: int) -> tuple[int, int]:
    return ((index) // n, index % n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, coordToIndex(m - 1, n - 1, n)

        while i + 1 < j:
            mid = (i + j) // 2
            midRow, midCol = indexToCoord(mid, n)
            midVal = matrix[midRow][midCol]
            if target == midVal:
                return True
            if target > midVal:
                i = mid
            elif target < midVal:
                j = mid
        
        iRow, iCol = indexToCoord(i, n)
        jRow, jCol = indexToCoord(j, n)
        return target in [matrix[iRow][iCol], matrix[jRow][jCol]]
