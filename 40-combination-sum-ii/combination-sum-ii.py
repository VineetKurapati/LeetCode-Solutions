from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sorting helps skip duplicates easily

        def dfs(start, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                # Skip duplicates to ensure each unique element is only used once per level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:  # No need to continue if element exceeds target
                    break
                dfs(i + 1, target - candidates[i], path + [candidates[i]])

        dfs(0, target, [])
        return result
