class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S = []
        T = []
        for char_s in s:
            S.append(char_s)
        for char_t in t:
            T.append(char_t)
        S.sort()
        T.sort()
        if S == T:
            return True
        return False
    
            
