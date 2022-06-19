# Date:       2020/9/2
# encode:      UTF-8

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 建立链表
def build(nums: list) -> ListNode:
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
def Print(head: ListNode) -> None:
    while head:
        print(head.val, end='')
        head = head.next
        if head:
            print(' ', end='')
        else:
            print()


# 反转链表
def reverseList(head: ListNode) -> ListNode:
    previous = None
    current = head
    while current is not None:
        nextNode = current.next
        current.next = previous
        previous = current
        current = nextNode
    return previous


# 删除排序链表中的重复元素2
def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    pre, cur = dummy, head
    while cur:
        flag = False
        while cur.next and cur.val == cur.next.val:
            flag = True
            cur = cur.next
        if flag:
            pre.next = cur.next
        else:
            pre = pre.next
        cur = cur.next
    return dummy.next


# 分割链表
def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
    n, temp = 0, head
    ans = [ListNode for _ in range(k)]
    while temp:
        temp = temp.next
        n += 1
    quotient, remainder = n // k, n - (n // k) * k
    index = 0
    curr = head
    while curr and index < k:
        ans[index] = curr
        part_size = quotient + (0 if remainder > 0 else -1)
        remainder -= 1
        while part_size and curr.next:
            part_size -= 1
            curr = curr.next
        next = curr.next
        curr.next = None
        curr = next
        index += 1
    return ans
