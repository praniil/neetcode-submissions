class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        contains = {}
        for num in nums:
            contains[num] = contains.get(num, 0) + 1

        for key, value in contains.items():
            if contains[key] > 1:
                res = True

        return res