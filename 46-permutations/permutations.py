class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        st = set()
        while(len(st) != factorial(len(nums))):
            shuffle(nums)
            st.add(tuple(nums))
        return st