class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        dict = {}

        for i, n in enumerate(sorted(nums)):
            if n not in dict:
                dict[n] = i
        return [dict[n] for n in nums]


# 1365. How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].