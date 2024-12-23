class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        self.levels = defaultdict(list)
        
        def dfs(root, level):
            if not root:
                return
            self.levels[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        count = 0
        for lvl in self.levels:
            temp = self.levels[lvl]
            sorted_temp = sorted(temp)
            index_map = {val: i for i, val in enumerate(sorted_temp)}
            visited = [False] * len(temp)
            for i in range(len(temp)):
                if visited[i] or index_map[temp[i]] == i:
                    continue
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = index_map[temp[x]]
                    cycle_size += 1
                if cycle_size > 1:
                    count += cycle_size - 1
        
        return count
