# -*- coding: utf-8 -*-
# File:      2043. 简易银行系统.py
# DATA:      2022/3/18
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Bank:

    # 使用下标从 0 开始的整数数组 balance 初始化该对象
    def __init__(self, balance: List[int]):
        self.n = (len(balance) + 1)
        self.accounts = [0] * self.n
        for i in range(len(balance)):
            self.accounts[i + 1] = balance[i]

    # 从编号为 account1 的账户向编号为 account2 的账户转帐 money 美元。如果交易成功，返回 true ，否则，返回 false
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.n or account2 > self.n:
            return False
        if self.accounts[account1] < money:
            return False
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True

    # 向编号为 account 的账户存款 money 美元。如果交易成功，返回 true ；否则，返回 false
    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        self.accounts[account] += money
        return True

    #  从编号为 account 的账户取款 money 美元。如果交易成功，返回 true ；否则，返回 false
    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        if self.accounts[account] < money:
            return False
        self.accounts[account] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
