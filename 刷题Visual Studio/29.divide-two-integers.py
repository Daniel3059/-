#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        d1 = abs(dividend)
        d2 = abs (divisor)
        cnt , times = 0,0
        while d1 >= d2:
            diff = d1 -(d2 << times) ## 记住加速
            if diff >= 0:
                cnt +=(1 <<times) ##记住加速
                times += 1
                d1 = diff
            else:
                times -= 1
        return max(-2**31,min(cnt*flag,2**31-1))

# @lc code=end

