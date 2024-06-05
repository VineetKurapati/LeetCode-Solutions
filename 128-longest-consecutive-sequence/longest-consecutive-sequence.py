from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        parents = {}
        size = {}

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])  # Path compression
            return parents[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parents[rootY] = rootX
                size[rootX] += size[rootY]

        for num in nums:
            if num not in parents:
                parents[num] = num
                size[num] = 1
                if num - 1 in parents:
                    union(num, num - 1)
                if num + 1 in parents:
                    union(num, num + 1)

        return max(size.values())