class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        contains = {}
        result = []
        for num in nums:
            contains[num] = contains.get(num, 0) + 1

        sorted_contains = dict(sorted(contains.items(), key=lambda item: (item[1], -item[0])))

        for key, value in sorted_contains.items():
            result.extend([key] * value)

        return result