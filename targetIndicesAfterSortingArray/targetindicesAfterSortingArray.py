# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedArr = sorted(nums)

        output = []
        for i, n in enumerate(sorted(nums)):
            if n== target:
                output.append(i)
        return output
    
    # Runtime = 0ms
    # Memory = 17.78 MB: beats 61.62%
