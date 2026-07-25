class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x: x[0])
        curr = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                ans.append(curr)
                curr = intervals[i]
            else:
                curr[1] = max(curr[1], intervals[i][1])
        
        ans.append(curr)

        return ans


        