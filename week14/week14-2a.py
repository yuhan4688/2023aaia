#leetcode 1662. Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
       a=''.join(word1)  #課本第2張的字串，有教
       b=''.join(word2)

       if a==b: return  True
       else: return False