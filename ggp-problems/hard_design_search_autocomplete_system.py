from collections import defaultdict, deque
import heapq


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.hashmap = defaultdict(int)
        for sentence, count in zip(sentences, times):
            self.putSentence(sentence, count)
        self.curr_search = ""

    def putSentence(self, sentence, times=1):
        if sentence in self.hashmap:
            self.hashmap[sentence] += 1
            return
        self.addToTrie(sentence)
        self.hashmap[sentence] += times

    def addToTrie(self, sentence):
        node = self.trie
        for char in sentence:
            node = node.setdefault(char, {})
        node["#"] = sentence

    def findInTrie(self, search_arr: str):
        candidates = []
        node = self.trie
        for i in search_arr:
            node = node.get(i, None)
            if node is None:
                return []
        queue = deque([node])
        while queue:
            node = queue.popleft()
            if "#" in node:
                candidates.append(node["#"])
            for key, child in node.items():
                if key != "#":
                    queue.append(child)
        return candidates

    def processFound(self, candidates):
        heap = []
        for can in candidates:
            heapq.heappush(heap, (-self.hashmap[can], can))

        ret = []
        for _ in range(min(len(candidates), 3)):
            item = heapq.heappop(heap)
            ret.append(item[1])

        return ret

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.putSentence(self.curr_search)
            self.curr_search = ""
            return []
        self.curr_search += c
        candidates = self.findInTrie(self.curr_search)
        return self.processFound(candidates)
