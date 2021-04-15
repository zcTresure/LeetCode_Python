import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.ns = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = val not in self.table
        if flag:
            self.table[val] = {len(self.ns), }
        else:
            self.table[val].add(len(self.ns))
        self.ns.append(val)
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        flag = val in self.table
        if flag:
            last_idx = len(self.ns) - 1
            v = self.ns[last_idx]
            index = self.table[val].pop()
            self.ns[index] = self.ns[last_idx]
            if last_idx != index:  # 如果只是最后一位的话，直接删除就好了
                self.table[v].remove(last_idx)
                self.table[v].add(index)
            if not len(self.table[val]): self.table.pop(val)

            self.ns.pop()
        return flag

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.ns)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
