class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        s = s.lower()
        for char in s:
            if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 48 and ord(char) <= 56):
                continue
            else:
                s = s.replace(char, "")
        left = 0 
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1               
                right -= 1
                continue
            else:
                res = False
                break
        return res