from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树的建立
def build(nums: list) -> TreeNode:
    if not nums: return None
    root = TreeNode(nums[0])
    nodes, index, n = [root], 1, len(nums)
    for node in nodes:
        if node != None:
            if index == n:
                return root
            node.left = TreeNode(nums[index]) if nums[index] != None else None
            nodes.append(node.left)
            index += 1
            if index == n:
                return root
            node.right = TreeNode(nums[index]) if nums[index] != None else None
            nodes.append(node.right)
            index += 1
    return root


# 层次遍历
def levelOrder(root: TreeNode) -> None:
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            print(node.val, end='')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if q:
                print(end=' ')
    print()


# 先序遍历
def preOrder(root: TreeNode) -> None:
    if not root:
        print('None', end=' ')
        return
    print(root.val, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# 中序遍历
def order(root: TreeNode) -> None:
    if not root:
        return
    order(root.left)
    print(root.val, end=' ')
    order(root.right)


# 后序遍历
def postorder(root: TreeNode) -> None:
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')


# 查找节点
def findNode(root: TreeNode, target: int) -> TreeNode:
    target_node = TreeNode(0)

    def dfs(node):
        if node:
            if node.val == target:
                target_node = node
                return
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return target_node
