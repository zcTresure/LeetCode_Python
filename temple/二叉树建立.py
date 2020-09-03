from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    # 先序遍历
    def preordPrint(self, root: TreeNode) -> None:
        if not root:
            return
        print(root.val, end=' ')
        self.preordPrint(root.left)
        self.preordPrint(root.right)

    # 中序遍历
    def orderPrint(self, root: TreeNode) -> None:
        if not root:
            return
        self.orderPrint(root.left)
        print(root.val, end=' ')
        self.orderPrint(root.right)

    # 后序遍历
    def postorderPrint(self, root: TreeNode) -> None:
        if not root:
            return
        self.postorderPrint(root.left)
        self.postorderPrint(root.right)
        print(root.val, end=' ')


so = Solution()
nums = [3, 2, 3, None, 3, None, 1]
root = so.constructTreeNodeDynamic(nums)
so.orderPrint(root)
print()
