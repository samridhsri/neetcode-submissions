class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((value, timestamp))
        
        else:
            self.hashMap[key] = self.hashMap.get(key, [])
            self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.hashMap:
            return res
        
        else:
            left, right = 0, len(self.hashMap[key]) - 1

            while(left <= right):
                mid = (left + right) // 2

                if(self.hashMap[key][mid][1] <= timestamp):
                    res = self.hashMap[key][mid][0]
                    left = mid + 1
                
                else:
                    right = mid - 1
            return res
        
