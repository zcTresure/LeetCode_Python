# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        arr = list()
        node = head
        while node:
            arr.append(node)
            node = node.next
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i == j:
                break
            arr[j].next = arr[i]
            j -= 1
        arr[i].next = None
        return head


arr = [1, 2, 3, 4, 5]
test = Solution()
head = test.build(arr)
head = test.reorderList(head)
test.Print(head)
