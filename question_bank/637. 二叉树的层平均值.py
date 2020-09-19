import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructTreeNodeDynamic(self, nums: list) -> TreeNode:
        if nums[0] == None:
            return None
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

    # 广搜
    def averageOfLevels(self, root: TreeNode) -> list:
        res = []
        q = collections.deque([root])
        while q:
            nodesum = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                nodesum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(nodesum / n)
        return res

    # 递归深搜
    def averageOfLevels(self, root: TreeNode) -> list:
        level_dic = collections.defaultdict(list)

        def dfs(node: TreeNode, depth: int) -> None:
            if node:
                level_dic[depth] += [node.val]
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root, 0)
        return list(sum(vals) / len(vals) for vals in level_dic.values())

    # 迭代深搜
    def averageOfLevels(self, root: TreeNode) -> list:
        level_dic = collections.defaultdict(list)
        stack, node, depth = [], root, -1
        while stack or node:
            while node:
                depth += 1
                stack.append((depth, node))
                level_dic[depth] += [node.val]
                node = node.left
            depth, node = stack.pop()
            node = node.right
        return list(sum(vals) / len(vals) for vals in level_dic.values())


nums = [3, 9, 20, None, None, 15, 17]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
print(test.averageOfLevels(root))
