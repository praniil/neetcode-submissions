class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False
        containsS = {}
        containsT = {}
        for c in s:
            containsS[c] = containsS.get(c, 0) + 1

        for c in t:
            containsT[c] = containsT.get(c, 0) + 1

        if containsS == containsT:
            res = True

        return res 