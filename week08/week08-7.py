class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #先做兩字串長度檢查
            return False #長度不同就失敗        
        
        d={} #空字典
        for c in s:
            if c in d :
                d[c]=d[c]+1
            else:
                d[c]=1
        #print(d)

        for c in t:
            if c not in d:
                return False
            if d[c]<=0:
                return False
            else:
                d[c]=d[c]-1

        return True