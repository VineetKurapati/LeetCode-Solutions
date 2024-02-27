class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
        # Update each element in the current row with the minimum path sum to reach it
            for j in range(len(triangle[i])):
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        # The minimum path sum to reach the top node will be stored in triangle[0][0]
        return triangle[0][0]