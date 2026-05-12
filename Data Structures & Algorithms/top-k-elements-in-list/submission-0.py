from heapq import heappushpop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        heap = []

        for num, freq in hmap.items():
            if len(heap) < k:
                heappush(heap, (freq, num))
            else:
                heappushpop(heap, (freq,num))

        ans = []
        for elem in heap:
            ans.append(elem[1])
        
        return ans
        