class TimeMap:

    def __init__(self):
        self.dic={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [[timestamp,value]]
        else:
            self.dic[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        arr = self.dic[key]
        start = 0
        end = len(arr) - 1
        ans = ""
        if timestamp < arr[0][0]:
            return ""
        while start<=end:
            mid = (start + end) // 2
            if timestamp == arr[mid][0]:
                return arr[mid][1]
            elif timestamp < arr[mid][0]:
                end = mid - 1
            else:
                ans = arr[mid][1]
                start = mid + 1
        return ans
