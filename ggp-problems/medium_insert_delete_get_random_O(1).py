import random


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        index = len(self.arr)
        self.map[val] = index
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        self.map[self.arr[-1]] = index
        self.arr[-1], self.arr[index] = self.arr[index], self.arr[-1]
        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
