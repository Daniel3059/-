#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [0]*n
        for i in range(n*2-1, -1, -1):
            while stack and nums[i % n] >= stack[-1] :
                stack.pop()
            res[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        return res
# TC: O(n) SC: O(n)
# @lc code=end

