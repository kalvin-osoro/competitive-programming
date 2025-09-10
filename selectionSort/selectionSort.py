class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        
        for i in range (n):
            temp = i
            for j in range (i+1, n):
                if (arr[j] < arr[temp]):
                    
                    temp = j
                    
            arr[i],arr[temp]= arr[temp], arr[i]
        return arr
            