class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        def differs(w1, w2):
            count = 0
            for a, b in zip(w1, w2):
                if a != b:
                    count += 1
            return count == 1 
        
        n = len(wordList)
        for i in range(n):
            for j in range(i + 1, n):
                if differs(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        if beginWord not in graph:
            for word in wordList:
                if differs(beginWord, word):
                    graph[beginWord].append(word)
                    graph[word].append(beginWord)
        queue = deque([(beginWord, 0)])
        vis = set(beginWord)
        while queue:
            curr_word, length = queue.popleft()
            if curr_word == endWord:
                return length + 1
            for w in graph[curr_word]:
                if w not in vis:
                    vis.add(w)
                    queue.append((w, length + 1))
        return 0
