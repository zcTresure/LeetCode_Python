# 插入排序
def diagonalSort(self, mat):
    i, j = 0, 0  # 从左上开始遍历
    n, m = len(mat), len(mat[0])
    while i < n and j < m:
        if i != 0 or j != 0:  # 插入排序第一个元素不用排序
            key = mat[i][j]
            k, t = i - 1, j - 1
            while k >= 0 and t >= 0 and mat[k][t] > key:
                mat[k + 1][t + 1] = mat[k][t]
                k -= 1
                t -= 1
            mat[k + 1][t + 1] = key
        # 下面是遍历条件，按列遍历
        if i < n - 1:
            i += 1
        else:
            i = 0
            j += 1
    return mat


# 快速排序
# def pitition(self, arr, low, high):
#     i = low - 1
#     key = arr[high]
#     for j in range(low, high):
#         if arr[j] < key:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# def quickSort(self, arr, low, high):
#     if low < high:
#         pi = self.pitition(arr, low, high)
#         self.quickSort(arr, low, pi - 1)
#         self.quickSort(arr, pi + 1, high)


# def diagonalSort(self, mat):

#     i, j = len(mat) - 1, 0  # 从左下往上，再往右遍历
#     n, m = len(mat), len(mat[0])
#     while j < m:
#         tmp = []
#         k, t = i, j
#         while k < n and t < m:  # 提取斜线方向的值
#             tmp.append(mat[k][t])
#             k += 1
#             t += 1
#         self.quickSort(tmp, 0, len(tmp) - 1)  # ***
#         k, t = i, j
#         while k < n and t < m:
#             mat[k][t] = tmp.pop(0)  # 替换排序后的值
#             k += 1
#             t += 1
#         if i > 0:  # 往上遍历
#             i -= 1
#         else:  # 往右遍历
#             j += 1
#     return mat


mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
print(diagonalSort(1, mat))
