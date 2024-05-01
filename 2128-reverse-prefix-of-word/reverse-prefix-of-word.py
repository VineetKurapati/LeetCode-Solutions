class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        temp = ""
        i = 0
        if ch not in word:
            return word
        n = len(word)
        while i < n:
            w = word[i]
            if w == ch:
                temp += w
                i+=1
                break
            else:
                temp+=w
            i+=1
        temp = reversed(temp)
        res = ""
        for w in temp:
            res+=w
        while i < n:
            res += word[i]
            i+=1
        return res
        