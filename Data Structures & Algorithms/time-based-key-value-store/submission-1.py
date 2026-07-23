class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        all_dataa = self.hashmap.get(key, [])
        left = 0 
        right = len(all_dataa) - 1
        while left <= right:
            mid = (left + right) // 2
            if all_dataa[mid][1] <= timestamp:
                res = all_dataa[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res