class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        interval = intervals[0]
        ret = []
        for i in range(1, len(intervals)):
            if interval[1] < intervals[i][0]:
                ret.append(interval)
                interval = intervals[i]
            else:
                interval[1] = max(interval[1], intervals[i][1])
        
        ret.append(interval)
        return ret
        