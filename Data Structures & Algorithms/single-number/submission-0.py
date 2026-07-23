class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        contains = {}
        for num in nums:
            contains[num] = contains.get(num, 0) + 1

        for key, value in contains.items():
            if contains[key] == 1:
                return key