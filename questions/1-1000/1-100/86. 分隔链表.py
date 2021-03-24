# Date:       2021/1/3
# encode:      UTF-8
__author__ = "zcTresure"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # 建立链表
    def build(self, nums: list) -> ListNode:
        if not nums:
            return None
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

    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = cur1 = ListNode(0)
        h2 = cur2 = ListNode(0)
        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
        cur1.next = h2.next
        cur2.next = None
        return h1.next


nums = [1, 4, 3, 2, 5, 2]
x = 3
test = Solution()
head = test.build(nums)
head = test.partition(head, 3)
test.Print(head)
