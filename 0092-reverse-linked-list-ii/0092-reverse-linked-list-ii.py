# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # sublist 시작 전 노드로 이동
        # 시작 전 노드로 이동
        for _ in range(left - 1):
            pre = pre.next

        current = pre.next
        next_node = None

        for _ in range(right -  left + 1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp
            
        # sublist의 시작 전 노드와 끝 다음 노드를 연결
        pre.next.next = current
        pre.next = next_node

        return dummy.next


        