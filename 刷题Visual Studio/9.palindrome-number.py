#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            i = 0
            j = len(x)-1
            while i < j:
                if x[i] != x[j]:
                    return False
                else:
                    i +=1
                    j -=1

        return True

# TC: O(n)  # SC:O(1) 用的双指针   
        
# @lc code=end

