# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 字典初始化   -1表示深度， TreeNode(0) 表示节点值为0的树
        tree = {-1: TreeNode(0)}

        def addNode(val, depth):              # 添加树函数
            tree[depth] = TreeNode(int(val))  # 当前节点值为val的树
            if not tree[depth - 1].left:      # 左子树不存在就加在左边     这个很好理解，同一个深度下先放在左子树
                tree[depth - 1].left = tree[depth]
            else:                             # 反之加在右边 第二次出现的同样深度的节点 就放在这里的右子树上
                tree[depth - 1].right = tree[depth]

        val, depth = '', 0                    # 值和对应深度初始化
        for c in S:
            if c != '-':
                val += c                       # 累加字符来获得数字 val初始值是'' 所以c是数字时和字符串相加，可得到对应的多位数的字符串
            elif val:                          # 如果是‘-’且存在val
                # 就把累加好的数字和对应深度添加进树     这里就去找有没有左子树，没有就加左边，有就加右边
                addNode(val, depth)
                val, depth = '', 1             # 值和对应深度重新初始化           加完一次初始化中间变量，再进行新一轮的计算
            else:
                depth += 1                     # 连续的‘-’只加深度不加值
        # 末尾剩余的数字也要加进树  最后一个节点值为一位数 会只在if判断里，所以要补充添加到树里
        addNode(val, depth)
        return tree[0] if tree else None


S = "1-2--3--4-5--6--7"
test = Solution()
print(test.recoverFromPreorder(S))
