# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        res = defaultdict(list)
        def getList(root, level):
            nonlocal res
            if not root:
                return
            res[level].append(root.val)
            if root.left:
                getList(root.left, level+1)
            if root.right:
                getList(root.right, level+1)
        getList(root, 0)
        even = False
        if len(res) == 1 and res[0][0] % 2 == 0:
            return False
        if res[0][0] % 2 == 0:
            even = True
        def checkIncreasing(arr):
            n = len(arr)
            for i in range(1, n):
                if arr[i-1] <= arr[i]:
                    return False
            return True
        def checkDecreasing(arr):
            n = len(arr)
            for i in range(1, n):
                if arr[i-1] >= arr[i]:
                    return False
            return True
        for i in range(1, len(res)):
            # If even check if its increasing 
            for x in res[i]:
                if x % 2 != 0 and not even:
                    return False
                if x % 2 == 0 and even:
                    return False
            if res[i][0] % 2 == 0:
                if not checkIncreasing(res[i]):
                    return False
            else:
                if not checkDecreasing(res[i]):
                    return False
            even = False if even else True
        return True