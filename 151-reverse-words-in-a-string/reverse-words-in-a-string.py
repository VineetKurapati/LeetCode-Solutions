class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l.reverse()
        res = ""
        print(l)
        for word in l:
            if word != '':
                res += word + " "
        return res[:-1]