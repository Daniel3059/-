#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        a = abs(x)
        while (a!=0):
            temp = a % 10 
            res = res * 10 + temp 
            a = a //10
        if x > 0 and res < 2**31:
            return res 
        elif x < 0 and res <= 2**31-1 :
            return -res
        else:
            return 0
        
# @lc code=end

