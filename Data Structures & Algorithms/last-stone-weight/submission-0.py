class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            stone1 = heapq.heappop_max(heap)
            stone2 = heapq.heappop_max(heap)

            if stone1 != stone2:
                heapq.heappush_max(heap, abs(stone1 - stone2))
        
        return heap[0] if len(heap) == 1 else 0