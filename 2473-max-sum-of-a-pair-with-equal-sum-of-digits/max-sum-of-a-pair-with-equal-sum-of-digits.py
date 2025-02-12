class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        c = defaultdict(list)
        def get_sum(n):
            count = 0
            while n:
                x = n % 10
                count += x
                n = n//10
            return count
        for n in nums:
            t = get_sum(n)
            c[t].append(n)
        res = float("-inf")
        for key, group in c.items():
            if len(group) >= 2:
                group.sort(reverse=True)  # Sort descending so the two largest numbers come first
                res = max(res, group[0] + group[1])
        return res if res != float("-inf") else -1