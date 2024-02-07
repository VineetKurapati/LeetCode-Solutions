class Solution:
    def frequencySort(self, s: str) -> str:
        dicti = {}
        for ch in s:
            if ch in dicti:
                dicti[ch]+=1
            else:
                dicti[ch] = 1
        dictii = dict(sorted(dicti.items(), key = lambda item : item[1]))
        res = ""
        for value in dictii:
            k = dictii[value]
            while k: 
                res+=value
                k-=1
        return res[::-1]
