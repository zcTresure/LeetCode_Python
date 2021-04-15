# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
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

    def Print(self, head: ListNode) -> None:
        while head:
            print(head.val, end='')
            head = head.next
            if head:
                print(' ', end='')
            else:
                print()

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        firstHalfEnd = self.endOfFirstHalf(head)
        secondHalfStart = self.reverseList(firstHalfEnd.next)
        firstPosition = head
        secondPosition = secondHalfStart
        while secondPosition:
            if firstPosition.val != secondPosition.val:
                return False
            firstPosition = firstPosition.next
            secondPosition = secondPosition.next
        firstHalfEnd.next = self.reverseList(secondHalfStart)
        return True

    def endOfFirstHalf(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current is not None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous


nums = [1, 2, 2, 11]
test = Solution()
head = test.build(nums)
test.Print(head)
print(test.isPalindrome(head))
test.Print(head)
