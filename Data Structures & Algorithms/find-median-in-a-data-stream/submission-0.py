class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))

        

    def findMedian(self) -> float:
        length_max = len(self.max_heap) 
        length_min = len(self.min_heap)

        if (length_max + length_min) % 2 == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        elif length_max > length_min:
            return self.max_heap[0]
        else:
            return self.min_heap[0]
        
        