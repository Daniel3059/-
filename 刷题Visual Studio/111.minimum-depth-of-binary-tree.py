#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
import queue


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Use BFS
        if not root :
            return 0
        queue = collections.deque()
        queue.append(root)
        depth = 1
        while queue:
            size = len(queue)
            for i in range (size):
                curr = queue.popleft()
                if not curr.left and not curr.right:
                    return depth
                if curr.left :
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depth += 1

        return depth 
# @lc code=end

