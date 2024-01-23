# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 함수는 연결 리스트의 길이를 계산하는 역할
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        lenA, lenB = get_length(headA), get_length(headB)
        
        # 두 리스트 길이 맞추기
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        
        while lenA < lenB:
            headB = headB.next
            lenB -=1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
            