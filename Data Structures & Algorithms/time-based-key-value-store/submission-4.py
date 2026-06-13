class TimeMap:

    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1

        while(l <= r):
            mid = (l + r) // 2

            if target == arr[mid][1]:
                return arr[mid][0]
            
            elif target > arr[mid][1]:
                l = mid + 1
            else:
                r = mid - 1
                
        return arr[r][0] if r >= 0 else ""

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        else:
            return self.binarySearch(self.timeMap[key], timestamp)
