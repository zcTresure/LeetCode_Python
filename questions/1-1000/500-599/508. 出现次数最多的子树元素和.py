# File Name:  508. 出现次数最多的子树元素和
# date:       2021/4/11
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List
from template import BinaryTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        all_sum = {}

        def heaper(node):
            if not node: return 0
            left_sum = heaper(node.left)
            right_sum = heaper(node.right)
            total = node.val + left_sum + right_sum
            all_sum[total] = all_sum.get(total, 0) + 1  # 记录每颗树上的总和
            return total

        heaper(root)
        sorted_all_sum = sorted(all_sum.items(), key=lambda x: x[1], reverse=True)  # 根据树总和出现的次数从大到小排列
        res = [sorted_all_sum[i][0] for i in range(len(sorted_all_sum)) if sorted_all_sum[i][1] == sorted_all_sum[0][1]]
        return res


nodes = [5, 2, -5, 2, -2]
test = Solution()
root = BinaryTree.build(nodes)
print(test.findFrequentTreeSum(root))
