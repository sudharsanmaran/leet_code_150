class TimeMap:

    def __init__(self):
        self.time_map = dict()
        self.time_stamp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[(key, timestamp)] = value
        self.time_stamp.setdefault(key, []).append(timestamp)  # timestamp sud be in accenting order

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.time_map:
            return self.time_map[(key, timestamp)]
        elif key in self.time_stamp:
            left, right, _max = 0, len(self.time_stamp[key]) - 1, -1
            while left <= right:
                mid = left + (right - left) // 2

                if self.time_stamp[key][mid] > timestamp:
                    right = mid - 1
                else:
                    _max = max(_max, mid)
                    left = mid + 1
            if _max > -1:
                return self.time_map[(key, self.time_stamp[key][_max])]
            else:
                return ""
        else:
            return ''


class TimeMap1:

    def __init__(self):
        self.time_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


if __name__ == '__main__':
    obj = TimeMap1()
    # obj.set('foo', 'bar', 1)
    # print(obj.get('foo', 1))
    # print(obj.get('foo', 3))
    obj.set('foo', 'bar2', 4)
    obj.set('foo', 'bar6', 6)
    print(obj.get('foo', 4))
    print(obj.get('foo', 5))
    print(obj.get('foo', 7))
