class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort(key=lambda x: x[1])
        skip = 0
        curr_interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < curr_interval[1]:
                skip += 1
            else:
                curr_interval = intervals[i]
        
        return skip


            
            
        

        