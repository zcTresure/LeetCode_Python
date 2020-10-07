class BrowserHistory:
    def __init__(self, homepage: str):
        # 初始化访问主页, 下标为0
        self.q = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        # 移除当前网页后面的所有网页
        while self.i < len(self.q) - 1:
            self.q.pop()
        self.q.append(url)
        self.i += 1

    def back(self, steps: int) -> str:
        # 新的下标要大于等于0
        self.i = max(0, self.i - steps)
        return self.q[self.i]

    def forward(self, steps: int) -> str:
        # 新的下标要小于列表长度
        self.i = min(len(self.q) - 1, self.i + steps)
        return self.q[self.i]

