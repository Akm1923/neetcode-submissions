class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:

        arr = sorted(self.data)
        n = len(arr)

        if n % 2:
            return arr[n // 2]

        return (arr[n//2 - 1] + arr[n//2]) / 2