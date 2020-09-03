# 官解
def generateTrees(self, n: int) -> list[TreeNode]:
    def generateTrees(start, end):
        if start > end:
            return [None,]
        allTrees = []
        for i in range(start, end + 1):
            leftTrees = generateTrees(start, i - 1)
            rightTrees = generateTrees(i + 1, end)
            for l in leftTrees:
                for r in rightTrees:
                    curTree = TreeNode(i)
                    curTree.left = l
                    curTree.right = r
                    allTrees.append(curTree)
        return allTrees
    return generateTrees(1, n) if n else []

