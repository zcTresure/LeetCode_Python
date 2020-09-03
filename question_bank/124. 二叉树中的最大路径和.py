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

    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
