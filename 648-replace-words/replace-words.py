class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = sentence.split()
        set_ = set(dictionary)
        res = ""
        for w in s:
            temp = ""
            n = len(res)
            for c in w:
                temp+=c
                if temp in set_:
                    res += temp + " "
                    break
            if n == len(res):
                res += temp + " "
        return res[:-1]

                