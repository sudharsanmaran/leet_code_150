import bisect


class MedianFinder:

    def __init__(self):
        self.data_stream = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.data_stream, num)

    def findMedian(self) -> float:
        median = None
        length = len(self.data_stream)
        if length % 2 == 0:
            left = (length - 1) // 2
            right = left + 1
            median = (self.data_stream[left] + self.data_stream[right]) / 2
        else:
            mid = length // 2
            median = self.data_stream[mid]
        return median


"""["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]"""

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
