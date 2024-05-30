class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0] + arr[:]
        n = len(prefix_xor)
        for i in range(1, n):
            prefix_xor[i] ^= prefix_xor[i-1]
        count = 0
        for start in range(n):
            for end in range(start + 1, n):
                if prefix_xor[start] == prefix_xor[end]:
                    count += end - start - 1
        return count