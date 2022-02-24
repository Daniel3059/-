#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    # 用 two pointer 解决
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        while left < right :
            maxarea = max(maxarea, min(height[left],height[right]) * (right-left))
            if height[left] < height [right]:
                left += 1
            else:
                right -= 1

        return maxarea
# TC: O(n) Single Pass
# SC: O(1) Constant Space is used 
# @lc code=end

