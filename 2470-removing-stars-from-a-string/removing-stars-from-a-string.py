class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for ch in s:
            if ch != "*":
                res.append(ch)
            else:
                res.pop()
        return "".join(res)