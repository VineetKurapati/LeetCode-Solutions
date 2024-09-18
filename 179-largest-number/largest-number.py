class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num = [str(n) for n in nums]
        num.sort(key=lambda a: a * 10, reverse=True)
        print(num)
        if num[0] == "0":
            return "0"
        return "".join(num)