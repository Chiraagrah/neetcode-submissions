class MedianFinder:
    '''
    Two Heaps, one store the lesser part of array, other stores higher part of array
    If both length 1 - length 2 > 1 or < -1 balance both of them
    If incomming element is > right's top most element add it to right else add it to left

    '''

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 :
            heapq.heappush(self.right,num)
            return
        elif num>self.right[0]:
            heapq.heappush(self.right,num)
            if len(self.right)>len(self.left):
                heapq.heappush(self.left,-heapq.heappop(self.right))
        else:
            heapq.heappush(self.left,-num)
            if len(self.right)<len(self.left):
                heapq.heappush(self.right,-heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.right)>len(self.left):
            return self.right[0]
        elif len(self.right)<len(self.left):
                return -self.left[0]
        else: 
            return (-self.left[0] + self.right[0]) /2
        