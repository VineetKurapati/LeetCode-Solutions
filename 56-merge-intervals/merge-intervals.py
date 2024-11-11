class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                res.append([start, end])
                start = intervals[i][0]
                end =  intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        res.append([start, end])
        return res