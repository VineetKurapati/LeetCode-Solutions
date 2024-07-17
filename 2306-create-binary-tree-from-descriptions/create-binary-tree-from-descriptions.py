class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        from collections import defaultdict

        # Step 1: Build map and identify potential roots
        m = defaultdict(list)
        children = set()
        for parent, child, is_left in descriptions:
            if parent not in m:
                m[parent] = [None, None]
            if is_left:
                m[parent][0] = child
            else:
                m[parent][1] = child
            children.add(child)
        root_val = (set(m.keys()) - children).pop()
        print(root_val)
        def buildtree(node_val):
            if node_val is None:
                return None
            node = TreeNode(node_val)
            if node_val in m:
                node.left = buildtree(m[node_val][0])
                node.right = buildtree(m[node_val][1])
            return node

        return buildtree(root_val)
