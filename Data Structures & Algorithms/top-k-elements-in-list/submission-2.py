class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        contains = {}
        for num in nums:
            contains[num] = contains.get(num, 0) + 1

        contains_sort = dict(sorted(contains.items(), key = lambda item: item[1], reverse=True))
        
        return list(contains_sort.keys())[:k]