class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        uniqueNums = set(nums)

        while len(uniqueNums) > 0:
            currentLen = 1
            originalValue = uniqueNums.pop()
            counter = originalValue + 1
            # check larger values
            while counter in uniqueNums:
                uniqueNums.remove(counter)
                counter += 1
            currentLen += counter - originalValue - 1

            # check smaller values
            counter = originalValue - 1
            while counter in uniqueNums:
                uniqueNums.remove(counter)
                counter -= 1
            currentLen += originalValue - counter - 1

            output = max(output, currentLen)
        
        return output
