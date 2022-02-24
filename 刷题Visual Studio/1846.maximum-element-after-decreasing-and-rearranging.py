#
# @lc app=leetcode id=1846 lang=python3
#
# [1846] Maximum Element After Decreasing and Rearranging
#

# @lc code=start
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted (arr)
        arr[0] = 1
        for i in range (len(arr)-1):
            if abs(arr[i+1]- arr[i]) > 1:
                arr[i+1] = arr[i] + 1
        return max(arr) 
# @lc code=end

