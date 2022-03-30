#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
           array = []
           dummy = head
           stack = []
           while dummy :
               array.append(dummy.val)
               dummy = dummy.next
           res = [0] * len(array)
           for i in range (len(array)-1, -1, -1):
               while stack and array[i] >= stack[-1]:
                   stack.pop()
               res[i] = stack[-1] if stack else 0
               stack.append(array[i])
           return res 
    # TC: O(N) SC: O(N)


# @lc code=end

