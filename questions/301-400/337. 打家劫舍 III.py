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

    # 暴力递归 - 最优子结构
    # 4 个孙子偷的钱 + 爷爷的钱 VS 两个儿子偷的钱
    # 哪个组合钱多，就当做当前节点能偷的最大钱数
    # 这就是动态规划里面的最优子结构
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        money = root.val
        if root.left:
            node = root.left
            money += self.rob(node.left) + self.rob(node.right)
        if root.right:
            node = root.right
            money += self.rob(node.left) + self.rob(node.right)
        return max(money, self.rob(root.left) + self.rob(root.right))

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def func(root):
            if not root:
                return 0, 0
            left_not_do, left_do = func(root.left)
            right_not_do, right_do = func(root.right)
            return max(left_not_do, left_do) + max(right_not_do, right_do), left_not_do + right_not_do + root.val
        return max(func(root))

    # 先序遍历
    def preordPrint(self, root: TreeNode) -> None:
        if not root:
            return
        print(root.val, end=' ')
        self.preordPrint(root.left)
        self.preordPrint(root.right)


test = Solution()
nums = [3, 2, 3, None, 3, None, 1]
root = test.constructTreeNodeDynamic(nums)
print(test.rob(root))
