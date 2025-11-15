import random


class RandomizedSet:

    def __init__(self):
        self.num_map: dict[int, int] = {}
        self.num_list: list[int] = []

    def get_index(self, val: int):
        return self.num_map.get(val, None)

    def insert(self, val: int) -> bool:
        index = self.get_index(val)
        if index is not None:
            return False
        self.num_list.append(val)
        self.num_map[val] = len(self.num_list) - 1
        return True

    def remove(self, val: int) -> bool:
        index = self.get_index(val)
        if index is None:
            return False

        swap_val = self.num_list[-1]
        self.num_list[index] = swap_val
        self.num_map[swap_val] = index

        _ = self.num_list.pop()
        del self.num_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)
