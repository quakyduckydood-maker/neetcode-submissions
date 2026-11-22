class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hush_s = {}
        hush_t = {}
        if len(s) != len(t):
            return False
        for i in s:
            hush_s[i] = 1 + hush_s.get(i,0)
        for i in t:
            hush_t[i] = 1 + hush_t.get(i,0)
        if hush_s == hush_t:
            return True
        else:
            return False
        


            
            