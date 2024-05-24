class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        d = {}
        ll = {}
        for i in range(len(score)):
            d[chr(i + 97)] = score[i]
            ll[chr(i+97)] = 0
        for l in letters:
            ll[l] += 1
        def converttoscore(word, ll):
            nonlocal d
            count = 0
            for c in word:
                if ll[c] == 0:
                    return 0
                else:
                    ll[c] -= 1
                    count+= d[c]
            return count
        word_score ={}
        for w in words:
            score = converttoscore(w, ll.copy())
            word_score[w] = score
        res = float("-inf")
        def isvalid(r):
            nonlocal ll
            temp_ll = ll.copy()
            for w in r:
                for c in w:
                    if temp_ll[c] == 0:
                        return False
                    else:
                        temp_ll[c] -= 1
            return True
        def evaluate(r):
            nonlocal word_score
            count = 0 
            for w in r:
                count += word_score[w]
            return count
        def backtrack(words, i, r):
            nonlocal res
            if i == len(words):
                if isvalid(r):
                    res = max(res, evaluate(r))
                return
            else:
                r.append(words[i])
                print(r)
                backtrack(words, i+1, r.copy())
                r.pop()
                backtrack(words, i+1, r.copy())
        backtrack(words, 0, [])
        return res



            
        