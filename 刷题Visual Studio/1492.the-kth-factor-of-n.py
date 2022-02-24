#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range (1, int(math.sqrt(n))+ 1):
            if n % i == 0 :
                k -= 1
                res.append(n //i )
            if k == 0:
                return (i)

        if res[-1] ** 2 == n :
            res .pop()

        return -1 if k > len(res) else res [-k]





        
# @lc code=end

