from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hori = defaultdict(set)
        vert = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in hori[i] or val in vert[j] or val in boxes[(i // 3, j // 3)]:
                    return False
                
                hori[i].add(val)
                vert[j].add(val)
                boxes[(i // 3, j // 3)].add(val)
        
        return True
