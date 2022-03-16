# -*- coding: utf-8 -*-
# File:      432. 全 O(1) 的数据结构.py
# DATA:      2022/3/16
# Software:  PyCharm
__author__ = 'zcFang'


class Node:
    # 双向链表
    def __init__(self, key="", count=0):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.count = count

    # 在 self 后插入 node
    def insert(self, node: 'Node') -> 'Node':
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    # 从链表中移除 self
    def remove(self):  # 从链表中移除 self
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:
    # 初始化数据结构的对象
    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root  # 初始化链表哨兵，下面判断节点的 next 若为 self.root，则表示 next 为空（prev 同理）
        self.nodes = {}

    # 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
    def inc(self, key: str) -> None:
        # key 不在链表中
        if key not in self.nodes:
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.count > cur.count + 1:
                self.nodes[key] = cur.insert(Node(key, cur.count + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if len(cur.keys) == 0:
                cur.remove()

    # 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中
    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1:  # key 仅出现一次，将其移出 nodes
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre is self.root or pre.count < cur.count - 1:
                self.nodes[key] = cur.prev.insert(Node(key, cur.count - 1))
            else:
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if len(cur.keys) == 0:
            cur.remove()

    # 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 ""
    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ""

    # 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 ""
    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
