class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # convert integers to strings

        array = list(map(str, nums))

        # custom sort with  lambda function
        array.sort(key = lambda x: x*10, reverse=True)

        #handle case where largest no is 0
        if array[0] == "0":
            return "0"
        

        #Build the largest number from the sorted array

        largest = ''.join(array)

        return largest


# https://leetcode.com/problems/largest-number/description/