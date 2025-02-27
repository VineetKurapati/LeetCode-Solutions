class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        max_len = 0
        for i in range(n):
            for j in range(i+1, n):
                a, b = arr[i], arr[j]
                length = 2
                while a + b in index:
                    a, b = b, a + b
                    length += 1
                if length >= 3:
                    max_len = max(max_len, length)
        return max_len
