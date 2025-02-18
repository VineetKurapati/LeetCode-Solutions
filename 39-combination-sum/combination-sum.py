class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = set()
        def backtrack(i, count, temp):
            if i >= len(candidates) or count > target:
                return 
            if count == target:
                res.add(tuple(temp.copy()))
            count += candidates[i]
            temp.append(candidates[i])
            backtrack(i, count, temp)
            backtrack(i + 1, count, temp)
            count -= candidates[i]
            temp.pop()
            backtrack(i + 1, count, temp)
        backtrack(0, 0, [])
        return [i for i in res]