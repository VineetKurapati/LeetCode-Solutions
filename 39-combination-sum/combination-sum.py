class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def backtrack(i, temp_sum, temp):
            if temp_sum == target:
                res.append(temp.copy())
                return
            if i >= n or temp_sum > target:
                return
            # If we take the next element
            temp_sum += candidates[i]
            temp.append(candidates[i])
            backtrack(i, temp_sum, temp) # Note: i is not incremented here because we can use the same element multiple times
            temp_sum -= candidates[i] # Revert the changes before backtracking
            temp.pop()
            # We don't consider the current element and go for the next element
            backtrack(i+1, temp_sum, temp)

        backtrack(0, 0, [])
        return res
