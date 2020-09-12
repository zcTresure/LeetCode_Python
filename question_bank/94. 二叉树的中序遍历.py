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

    # 中序遍历 递归形式
    def inorderTraversal(self, root: TreeNode) -> list:
        res = list()

        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

    # 中序遍历 迭代形式
    def inorderTraversal(self, root: TreeNode) -> list:
        stack = list()
        res = list()

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


nums = [1, None, 2, 3]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
print(test.inorderTraversal(root))
