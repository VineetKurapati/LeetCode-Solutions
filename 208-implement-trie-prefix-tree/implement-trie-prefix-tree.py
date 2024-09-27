class Trie:

    def __init__(self):
        self.s = set()
        self.words = set()

    def insert(self, word: str) -> None:
        c = ""
        self.words.add(word)
        for i in word:
            self.s.add(c)
            c += i
        self.s.add(c)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.s


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)