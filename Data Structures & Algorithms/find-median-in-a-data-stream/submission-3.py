class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
        elif num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) - len(self.maxHeap) > 1:
                heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))
        else:
            heapq.heappush_max(self.maxHeap, num)
            if len(self.minHeap) < len(self.maxHeap):
                heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))
            

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
    
        
        