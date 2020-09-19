import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 中序遍历
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            # 选择中间位置左边的数字作为根节点
            mid = (left + right) // 2
            # 选择中间位置右边的数字作为根节点
            # mid = (left + right + 1) // 2
            # 选择任意一个中间位置数字作为根节点
            # mid = (left + right + randint(0, 1)) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)


    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if not nums:
            return None
        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

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

nums = [-10,-3,0,5,9]
test = Solution()
root = test.sortedArrayToBST(nums)
test.levelorderPrint(root)