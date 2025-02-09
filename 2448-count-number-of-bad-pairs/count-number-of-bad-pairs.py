class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        m = defaultdict(int) 
        n = len(nums)
        total_pairs = ceil(n*(n-1)/2)
        for i in range(n):
            c = nums[i] - i
            m[c] += 1
        total_good_pairs = 0 
        for i in m:
            if m[i] > 1:
                total_good_pairs += (m[i] * (m[i] - 1)) // 2
        print(m)
        return total_pairs - total_good_pairs