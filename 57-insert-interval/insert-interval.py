class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        # Merge the Interval 
        start = intervals[0][0]
        end = intervals[0][1]
        n = len(intervals)
        res = []
        for i in range(1, n):
            new_start, new_end = intervals[i][0], intervals[i][1]
            if end >= new_start:
                end = max(end, new_end)
            else:
                res.append([start, end])
                start = new_start
                end = new_end
        res.append([start, end])
        return res