class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            cur = head
            pre = head = None
            while cur:
                if cur.left:
                    if not pre:
                        pre = head = cur.left
                    else:
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if not pre:
                        pre = head = cur.right
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next
        return root