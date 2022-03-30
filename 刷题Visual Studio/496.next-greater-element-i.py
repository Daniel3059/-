#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 用单调栈 + 字典
        stack = []
        dic = {}
        for i in range (len(nums2)-1, -1, -1 ): # Monotonic stack , increasing 
            n = nums2[i]
            while stack and stack[-1] < n:
                stack.pop()
            dic[n] = stack[-1] if stack else -1
            stack.append(n)
        return [dic[j] for j in nums1]
#  https://leetcode-cn.com/problems/next-greater-element-i/solution/dan-diao-zhan-jie-jue-next-greater-number-yi-lei-w/

# TC: O（n) SC: O(n)
# @lc code=end

