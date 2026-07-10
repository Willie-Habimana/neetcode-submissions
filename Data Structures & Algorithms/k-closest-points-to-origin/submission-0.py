class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1])**2)
            if len(heap) < k:
                heapq.heappush_max(heap, (distance, point))
            else:
                heapq.heappushpop_max(heap, (distance, point))
        

        return [val[1] for val in heap]
        