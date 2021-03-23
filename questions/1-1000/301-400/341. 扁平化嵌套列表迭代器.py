# File Name:  341. 扁平化嵌套列表迭代器
# date:       2021/3/23
# Coding:      UTF-8
__author__ = 'zcTresure'

import collections


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def dfs(self, nests):
        for nest in nests:
            if nest.isInteger():  # 如果当前序列是一个整数，存入队列中
                self.queue.append(nest.getInteger())
            else:  # 否者是一个列表，继续递归，直到当前对象为整数时
                self.dfs(nest.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque()  # 存储每个列表中的整数
        self.dfs(nestedList)  # 深度搜索每个列表

    def next(self) -> int:
        return self.queue.popleft()  # 按队列先后顺序出队列

    def hasNext(self) -> bool:
        return len(self.queue)  # 返回整个队列


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []  # 用栈逆序存储该列表或整数对象的长度
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        cur = self.stack.pop()  # 栈顶元素为整数，直接输出
        return cur.getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1]  # 记录栈顶元素
            if cur.isInteger():  # 栈顶元叔为整数时，直接返回输出
                return True
            self.stack.pop()  # 否则为一个列表，弹出栈顶元素
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])  # 逆序存储列表递归列表长度
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
