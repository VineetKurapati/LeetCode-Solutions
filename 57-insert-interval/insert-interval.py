class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        # Now merge these intervals 
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        res.append([start, end])
        return res