class Solution:
    def sortSentence(self, s: str) -> str:

       #split the sentence into an array of strings
       #obtain the last index and convert into an integer
       #sort based on the integer value 
       #bring the strings together
        word_list = s.split()
        ans = []
        for i in word_list:
            ele_idx = int(i[-1])
            ans.insert(ele_idx-1,i[:-1])
        result = ' '.join(ans)
        return result