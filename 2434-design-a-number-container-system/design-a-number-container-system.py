class NumberContainers:
    def __init__(self):
        self.s = defaultdict(int)
        self.num = defaultdict(SortedSet)
    def change(self, index: int, number: int) -> None:
        if index in self.s and self.s[index] != number:
            self.num[self.s[index]].remove(index)
        self.s[index] = number
        self.num[number].add(index)
    def find(self, number: int) -> int:
        if number not in self.num or not self.num[number]:
            return -1 
        return self.num[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)