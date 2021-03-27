# File Name:  61. 旋转链表
# date:       2021/3/27
# encode:      UTF-8
__author__ = 'zcTresure'

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 建立链表
    def build(self, nums: list) -> ListNode:
        if not nums:
            return ListNode(-1)
        head = ListNode(nums[0])
        pre = head
        for i in range(1, len(nums)):
            cur = ListNode(nums[i])
            pre.next = cur
            pre = pre.next
        return head

    # 打印链表
    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    # 旋转链表
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        link_length = 1  # 链表长度
        pre = head
        while pre.next:
            link_length += 1
            pre = pre.next
        pre.next = head  # 闭合链表，构建循环链表
        split = link_length - (k % link_length)  # 处理应该移动的位置
        while split:
            head = head.next
            pre = pre.next
            split -= 1
        pre.next = None  # 链表尾置空，断开循环链表
        return head


nums = [1, 2, 3, 4]
k = 5
test = Solution()
head = test.build(nums)
test.Print(head)
head = test.rotateRight(head, k)
test.Print(head)
