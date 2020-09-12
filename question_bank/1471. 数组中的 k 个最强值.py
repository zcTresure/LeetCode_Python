class Solution:
    def getStrongest(self, arr: list, k: int) -> list:
        n = len(arr)
        # 先排序求中位数
        arr = sorted(arr)
        mid = arr[(n - 1) // 2]

        def mykey(x):
            # 自定义最强排序的key函数
            # 注意py 3不同于其他语言的传入两个参数的自定义比较函数
            # 此处的意思代表先按照abs升序排列, 相等情况下再按照自身的值的升序排列
            return (abs(x - mid), x)

        # 按照最强排序后取最后的k个即为所求
        arr = sorted(arr, key=mykey)
        return arr[n - k:]
