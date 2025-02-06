class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != nums[j]:
                    c = nums[i] * nums[j]
                    d[c] +=1
        res = 0
        for c in d:
            if d[c] >= 2:
                count = d[c]
                res += 8 * (count * (count - 1) // 2)
        return res


