class TimeMap:

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key: str, value: str, timeStamp: int) -> None:
        if key in self.hashMap:
            self.hashMap[key].append((value,timeStamp))
        else:
            self.hashMap[key] = [(value,timeStamp)]

    def get(self, key: str, timeStamp: int) -> str:
        res = ""
        if key not in self.hashMap:
            return res
        
        else:
            l,r = 0, len(self.hashMap[key]) - 1
            valueArr = self.hashMap[key]

            while (l<=r):
                mid = (l+r)//2
                if(valueArr[mid][1]<=timeStamp):
                    res = valueArr[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        
