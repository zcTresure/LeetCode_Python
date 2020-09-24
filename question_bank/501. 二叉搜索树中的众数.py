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

    # 深度优先搜索
    def findMode(self, root: TreeNode) -> list:
        if not root:
            return []
        count = {}

        def dfs(node: TreeNode):
            if not node:
                return
            if node.val not in count:
                count[node.val] = 1
            else:
                count[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        maxval = max(count.values())
        res = []
        for k, v in count.items():
            if maxval == v:
                res.append(k)
        return res

    # 广度优先搜索
    def findMode(self, root: TreeNode) -> list:
        if not root:
            return []
        count = collections.defaultdict(int)
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.val not in count:
                count[node.val] = 1
            else:
                count[node.val] += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        maxval = max(count.values())
        res = []
        for k, v in count.items():
            if maxval == v:
                res.append(k)
        return res

    # 中序遍历
    def findMode(self, root: TreeNode) -> list:
        def inorde(node: TreeNode):
            if not node:
                return
            nonlocal ans, most, last, cnt
            inorde(node.left)
            if node.val == last:
                cnt += 1
            else:
                cnt = 1
            if cnt == most:
                ans.append(node.val)
            elif cnt > most:
                ans.clear()
                most = cnt
                ans.append(node.val)
            last = node.val
            inorde(node.right)
        ans, most, last, cnt = [], 0, None, 0
        inorde(root)
        return ans


test = Solution()
nums = [1, None, 2, 2]
root = test.constructTreeNodeDynamic(nums)
print(test.findMode(root))
