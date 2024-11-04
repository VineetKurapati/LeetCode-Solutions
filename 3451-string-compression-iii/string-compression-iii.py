class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        n = len(word)
        i = 0 
        while i < n:
            count = 0 
            j = i 
            while j < n and word[j] == word[i] and count < 9:
                count += 1
                j+=1
            s = str(count)
            comp += s
            comp += word[i]
            i = j
        return comp