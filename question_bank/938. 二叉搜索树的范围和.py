# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


class Solution:
    def constructTreeNodeDynamic(self, TreeNodeList: list) -> TreeNode:
        q = Queue(len(TreeNodeList))
        root = pre = TreeNode(TreeNodeList[0])
        for i in range(1, len(TreeNodeList)):
            if TreeNodeList[i] == None:
                continue
            cur = TreeNode(TreeNodeList[i])
            if i % 2 == 1:
                pre.left = cur
                q.put(pre.left)
            else:
                pre.right = cur
                q.put(pre.right)
                if not q.empty():
                    pre = q.get()
        return root

    # 递归实现深度优先搜索
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

    # 迭代实现深度优先搜索
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans


root = [10, 5, 15, 3, 7, None, 18]
L, R = 7, 15
test = Solution()
head = test.constructTreeNodeDynamic(root)
print(test.rangeSumBST(head, L, R))
