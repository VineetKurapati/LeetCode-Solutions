class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            for j in range(1, i):
                curr_val = res[i - 1][j-1] + res[i-1][j]
                temp[j] = curr_val
            res.append(temp)
        return res