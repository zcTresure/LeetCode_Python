import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return TreeNode(-1)
        root = TreeNode(nums[0])
        Nodes, index = [root], 1
        for node in Nodes:
            if node != None:
                node.left = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.left)
                index += 1
                if index == len(nums):
                    return root
                node.right = TreeNode(
                    nums[index]) if nums[index] != None else None
                Nodes.append(node.right)
                index += 1
                if index == len(nums):
                    return root

    # 前序遍历递归实现
    def flatten(self, root: TreeNode) -> None:
        preorderlist = list()

        def preordertraversal(root: TreeNode):
            if root:
                preorderlist.append(root)
                preordertraversal(root.left)
                preordertraversal(root.right)
        preordertraversal(root)
        for i in range(1, len(preorderlist)):
            prev, cur = preorderlist[i - 1], preorderlist[i]
            prev.left = None
            prev.right = cur

    # 前序遍历迭代实现
    def flatten(self, root: TreeNode) -> None:
        preorderlist = list()
        stack = list()
        node = root
        while node or stack:
            while node:
                preorderlist.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        for i in range(1, len(preorderlist)):
            prev, cur = preorderlist[i - 1], preorderlist[i]
            prev.left = None
            prev.right = cur

    # 前序遍历和展开同步进行

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            cur = stack.pop()
            if prev:
                prev.left = None
                prev.right = cur
            left, right = cur.left, cur.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = cur

    # 寻找前驱节点
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                predecessor = nxt = cur.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right

    def levelorderPrint(self, root: TreeNode) -> None:
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            print(node.val, end='')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if q:
                print(end=' ')
        print()


nums = [1, 2, 5, 3, 4, 6]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
test.flatten(root)
test.levelorderPrint(root)
