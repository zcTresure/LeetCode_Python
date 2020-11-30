# File Name:  ${NAME}
# date:       ${DATE}
__author__ = "zcTresure"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def build(self, nums: list) -> ListNode:
        if not nums:
            return
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

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even = evenHead = cur = head.next
        flag = True
        while cur:
            cur = cur.next
            if flag:
                flag = False
                odd.next = cur
                if cur:
                    odd = odd.next
            else:
                flag = True
                even.next = cur
                even = even.next
        if cur:
            odd.next = cur
            odd = odd.next
        odd.next = evenHead
        return head


nums = [1, 2, 3, 4, 5]
test = Solution()
link = test.build(nums)
link = test.oddEvenList(link)
test.Print(link)
