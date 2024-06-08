class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = []
        for i in range(n):
            t = []
            for j in range(i+1):
                if j == 0 or j == i:
                    t.append(1)
                else:
                    t.append(res[i-1][j-1] + res[i-1][j])
            res.append(t)
        return res

