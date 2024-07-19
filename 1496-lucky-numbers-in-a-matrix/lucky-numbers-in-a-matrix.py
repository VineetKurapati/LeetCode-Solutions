class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        max_col = {}
        min_row = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col not in max_col:
                    max_col[col] = matrix[row][col]
                if row not in min_row:
                    min_row[row] = matrix[row][col]
                min_row[row] = min(min_row[row], matrix[row][col])
                max_col[col] = max(max_col[col], matrix[row][col])
        print(max_col)
        print(min_row)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                curr_max_col = max_col[j]
                curr_min_row = min_row[i]
                curr_ele = matrix[i][j]
                print("current ele: " + str(curr_ele) + " row: " + str(i) + " col: " + str(j))
                if curr_ele == curr_min_row and curr_ele == curr_max_col:
                    res.append(curr_ele)

        return res