class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def helper(open_count, close_count, current):
            if open_count == n and close_count == n:
                res.add(current)
                return 
            if open_count < n:
                helper(open_count + 1, close_count, current + '(')
            if open_count > close_count:
                helper(open_count, close_count + 1, current + ')')
        
        helper(0, 0, "")
        return list(res)
