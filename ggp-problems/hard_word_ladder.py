import string
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        wordList.discard(beginWord)
        queue = deque([(beginWord, 1)])
        while queue:
            word, sequence = queue.popleft()
            if word == endWord:
                return sequence
            for i in range(len(word)):
                copy = list(word)
                for j in list(string.ascii_lowercase):
                    copy[i] = j
                    copy_str = "".join(copy)
                    if copy_str in wordList:
                        queue.append((copy_str, sequence + 1))
                        wordList.remove(copy_str)
        return 0
