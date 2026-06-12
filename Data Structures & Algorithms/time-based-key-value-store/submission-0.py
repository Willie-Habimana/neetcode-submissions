class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]

        l = 0
        r = len(values) - 1
        ans = ""
        while l <= r:
            mid = (l+r) // 2

            if values[mid][1] > timestamp:
                r = mid - 1
            elif values[mid][1] < timestamp:
                ans = values[mid][0]
                l = mid + 1
            else:
                return values[mid][0]
        
        return ans
        
