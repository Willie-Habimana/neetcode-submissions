class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        currInterval = intervals[0]
        for i in range(1, len(intervals)):
            if currInterval[1] > intervals[i][0]:
                count += 1
                if currInterval[1] > intervals[i][1]:
                    currInterval = intervals[i]
            else:
                currInterval = intervals[i]
        
        return count
        