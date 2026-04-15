# 2. Add New Numbers



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 結果を格納するための器
        dummy = ListNode(0)
        # 現在の書き込み位置を指すポインタ
        curr = dummy
        # 繰り上がりを保存する変数
        carry = 0

        
'''
AIと一緒にやったけど全くわからず。
・連結リスト（Linked List）とNodeについて、ちゃんと理解したい。
・ダミーノードの考え方
'''