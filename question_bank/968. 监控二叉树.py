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

    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> list:
            if not root:
                return [float("inf"), 0, 0]
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]
        a, b, c = dfs(root)
        return b

    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def lrd(node):
            if node is None:
                return 1  # 空节点不需要被人拍也不用拍别人，直接返回被拍了就好
            left = lrd(node.left)
            right = lrd(node.right)
            if left == 0 or right == 0:
                # 如果左儿子或者右儿子需要被拍，我就装个摄像机
                self.res += 1
                return 2
            if left == 2 or right == 2:
                # 如果左儿子或者右儿子装了摄像机，那我就被拍了
                return 1
            else:  # left == 1 and right == 1:
                # 如果左儿子和右儿子都是被拍的，都没有摄像机，那我就是需要被拍的状态
                return 0
        if lrd(root) == 0:
            # 看看根节点是不是需要被拍
            self.res += 1
        return self.res

    # 层次遍历
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


nums = [0, 0, None, 0, 0]
test = Solution()
root = test.constructTreeNodeDynamic(nums)
test.levelorderPrint(root)
print(test.minCameraCover(root))
