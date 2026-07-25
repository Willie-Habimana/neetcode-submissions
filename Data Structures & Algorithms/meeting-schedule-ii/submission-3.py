"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda x: x.start)
        next_available = [intervals[0].end]
        rooms = 1
        for i in range(1, len(intervals)):
            if intervals[i].start < next_available[0]:
                rooms += 1
            else:
                heapq.heappop(next_available)
            heapq.heappush(next_available, intervals[i].end)
        return rooms

        