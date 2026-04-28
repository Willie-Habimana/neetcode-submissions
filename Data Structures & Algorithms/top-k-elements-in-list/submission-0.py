
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num, c in count.items():
            if len(heap) < k:
                heappush(heap, (c, num))
            else:
                heappushpop(heap, (c, num))
        
        return [tup[1] for tup in heap]