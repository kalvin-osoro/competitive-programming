class Solution:
  def checkIfPangram(self, sentence):
    # TODO: Write your code here
    seen = set()

    for i in range(len(sentence)):

      currChar = sentence[i].lower()
      if currChar.isalpha():
        seen.add(currChar)
    return len(seen) == 26
    # return False
