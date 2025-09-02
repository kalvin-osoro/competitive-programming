# Problem Statement
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# brute force solution

class Solution:
    def containsDuplicate(self, nums):
      # TODO: Write your code here
      for i in range(len(nums)):
        for j in range(i+1, len(nums)):
          if(nums[i]== nums[j]):
            return True
      return False


# test cases

# [1,2,3,4]
# [1,2,3,1]
# [3, 2, 6, -1, 2, 1]
