class Solution:
    pairs = {"(": ")", "{": "}", "[": "]"}

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in Solution.pairs.keys():
                stack.append(c) 
            elif c in Solution.pairs.values():
                if len(stack) == 0 or not self.canClose(stack.pop(), c):
                    return False
        
        return len(stack) == 0

    def canClose(self, left: str, right: str) -> bool:
        return Solution.pairs[left] == right
