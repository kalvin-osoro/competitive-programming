class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorsArr = []
        for i in range(len(nums)-1):
            for j in range (len(nums)-1):
                temp = nums[i]
                if nums[j] > nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
                    
                    # above solution is bubble sort, not efficient especially for large arrays
                    
                    # use Dutch national Flag algo to sort it 
                    
                    
                    
                    # https://leetcode.com/problems/sort-colors/submissions/1779501361/
                    
                    # solve using counting sort, then overite the list