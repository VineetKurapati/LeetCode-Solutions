class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        curr_color = image[sr][sc]
        def dfs(i, j):
            if i < 0 or j < 0 or i >=n or j>=m or image[i][j] != curr_color or image[i][j] == color:
                return 
            image[i][j] = color
            dire = [[1, 0], [-1, 0], [0, 1], [0,-1]]
            for x, y in dire:
                dfs(i+x, j+y)
        dfs(sr, sc)
        return image