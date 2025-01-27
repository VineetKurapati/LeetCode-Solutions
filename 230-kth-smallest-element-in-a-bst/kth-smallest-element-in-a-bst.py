class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            if count[0] == 1:
                ans[0] = root.val
            count[0] -= 1
            if count[0] > 0:
                dfs(root.right)
        
        dfs(root)
        return ans[0]
            