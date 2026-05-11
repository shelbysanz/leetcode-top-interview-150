from collections import defaultdict


class Logger:

    def __init__(self):
        self.hashmap = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.hashmap and timestamp < self.hashmap[message]:
            return False
        self.hashmap[message] = timestamp + 10
        return True
