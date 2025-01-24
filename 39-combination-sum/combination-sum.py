class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = set()
        def backtrack(temp, i, count):
            if count > target or i >= len(candidates):
                return 
            if count == target:
                res.add(tuple(temp.copy()))
                return 
            temp.append(candidates[i])
            backtrack(temp, i +1, count + candidates[i])
            backtrack(temp, i, count + candidates[i])
            temp.pop()
            backtrack(temp, i +1, count)
            return 
        backtrack([], 0, 0)
        return [i for i in res]
