class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_string = []
        right_string = []
        left = 0
        right = len(s)
        for i in range(len(s)):
            if s[left+i].isalnum():
                left_string.append(s[left+i].lower())
            else:
                pass
            if s[right-1-i].isalnum():
                right_string.append(s[right-1-i].lower())
        d = "".join(right_string)
        f = "".join(left_string)
        if d == f:
            return True
        return False    