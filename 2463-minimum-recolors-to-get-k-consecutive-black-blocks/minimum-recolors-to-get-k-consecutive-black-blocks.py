class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_recolors = float("inf")
        count_w = blocks[:k].count('W')
        min_recolors = count_w
        for i in range(k, n):
            if blocks[i-k] == "W":
                count_w -=1 
            if blocks[i] == "W":
                count_w +=1 
            min_recolors = min(min_recolors, count_w)
        return min_recolors