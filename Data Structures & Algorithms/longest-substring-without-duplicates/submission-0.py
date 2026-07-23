class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        subset = set()
        for right in range(len(s)):
            while s[right] in subset:
                subset.remove(s[left])
                left += 1
            
            subset.add(s[right])
            maxlen = max(maxlen, right - left + 1)

        return maxlen 
