class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n:
            sum += n % 2
            n = n >> 1
        return sum