# -*- coding: utf-8 -*-
# File:      面试题 16.25. LRU 缓存.py
# DATA:      2022/5/31
# Software:  PyCharm
__author__ = 'zcFang'

from collections import OrderedDict


# class LRUCache(OrderedDict):
#
#     def __init__(self, capacity: int):
#         super.__init__()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]  # 如果 key 存在，先通过哈希表定位，再移到头部
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:  # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            self.cache[key] = node  # 添加进哈希表
            self.addToHead(node)  # 添加至双向链表的头部
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()  # 如果超出容量，删除双向链表的尾部节点
                self.cache.pop(removed.key)  # 删除哈希表中对应的项
                self.size -= 1
        else:  # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node: DLinkedNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node: DLinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node: DLinkedNode):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


cache = LRUCache(2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
