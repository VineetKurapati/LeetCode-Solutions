class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        n = len(points)
        points.sort(key = lambda x: x[1])
        print(points)
        start = points[0][0]
        end = points[0][1]
        res = []
        for i in range(1, n):
            if end < points[i][0]:
                count += 1
                start = points[i][0]
                end = points[i][1]
        count += 1
        return count