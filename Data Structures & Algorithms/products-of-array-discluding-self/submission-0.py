import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 0
        res = [0] * len(nums)
        while left <= len(nums) - 1:
            product = 1
            if left == 0:
                product = math.prod(nums[left + 1: len(nums)])
                res[left] = product
                left = left + 1
            else:
                product = math.prod(nums[0:left]) * math.prod(nums[left+1: len(nums)])
                res[left] = product
                left = left + 1

        return res
            