from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_x, start_y = entrance

        # Directions for movement: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = deque([(start_x, start_y, 0)])  # (x, y, steps)
        maze[start_x][start_y] = '+'  # Mark the entrance as visited
        
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    if nx == 0 or ny == 0 or nx == rows - 1 or ny == cols - 1:
                        return steps + 1
                    maze[nx][ny] = '+'  # Mark as visited
                    queue.append((nx, ny, steps + 1))
        
        return -1
