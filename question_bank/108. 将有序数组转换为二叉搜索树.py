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
