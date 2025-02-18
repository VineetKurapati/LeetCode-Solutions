class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = set()
        def backtrack(i, count, temp):
            if i >= len(candidates) or count > target:
                return 
            if count == target:
                res.add(tuple(temp.copy()))
            temp.append(candidates[i])
            backtrack(i, count + candidates[i], temp)
            backtrack(i + 1, count + candidates[i], temp)
            temp.pop()
            backtrack(i + 1, count, temp)
        backtrack(0, 0, [])
        return [i for i in res]