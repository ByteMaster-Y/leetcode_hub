# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # 결과 연결 리스트의 더미 노드
        current = dummy # 현재 노드를 가리키는 포인터
        carry = 0
        
        while l1 or l2 or carry:
            # 두 연결 리스트의 현재 자릿수의 합과 올림값을 더하여 계산
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            # 합을 이용하여 새로운 노드 생성
            # sum_val이 15일 경우, divmod(15, 10)은 (1, 5)를 반환합니다. 
            # 여기서 1은 다음 자릿수로 넘어가는 올림이 되고, 5는 현재 자릿수의 값이 됩니다.
            carry, digit = divmod(sum_val, 10)
            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next
            
        