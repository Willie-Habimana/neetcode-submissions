class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        clock = 0
        task_counter = Counter(tasks)
        heap = [(count, -math.inf) for _, count in task_counter.items()]
        heapq.heapify_max(heap)

        while heap: 
            count, time = heapq.heappop_max(heap)
            saved = []
            while heap and clock - time <= n:
                saved.append((count, time))
                count, time = heapq.heappop_max(heap)
            
            if clock - time > n:
                print("found")
                count -= 1
                if count > 0:
                    heapq.heappush_max(heap, (count, clock))
            else:
                heapq.heappush_max(heap, (count, time))

            for s in saved:
                heapq.heappush_max(heap, (s[0], s[1]))
            
            clock +=1 
            
        
        return clock
        

        