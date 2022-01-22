# -*- coding: utf-8 -*-
# File:    2034. 股票价格波动.py
# Date:    2022/1/23
# Software: Pycharm
__author__ = 'zcFang'

from sortedcontainers import SortedList


class StockPrice:

    def __init__(self):
        self.price = SortedList()
        self.time_price_map = {}
        self.max_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_price_map:
            self.price.discard(self.time_price_map[timestamp])
        self.price.add(price)
        self.time_price_map[timestamp] = price
        self.max_timestamp = max(self.max_timestamp, timestamp)

    def current(self) -> int:
        return self.time_price_map[self.max_timestamp]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
