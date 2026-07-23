class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        for ch in s1:
            dict1[ch] = dict1.get(ch, 0) + 1

        left = 0
        right = len(s1)
        while right <= len(s2):
            dict2 = {}
            for ch in s2[left:right]:
                dict2[ch] = dict2.get(ch, 0) + 1

            if dict1 == dict2:
                return True
            
            left += 1
            right += 1
        
        return False