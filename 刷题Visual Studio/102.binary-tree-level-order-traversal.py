#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            temp =[] # 每走一层，curent list（temp） 都是新的
            for i in range(len(queue)): # 这里是这一层遍历
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left :
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(temp)
        return res 

# @lc code=end

