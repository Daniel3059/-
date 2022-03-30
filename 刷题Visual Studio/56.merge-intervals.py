#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
     #根据soultion写的
     # sorting 方法
     intervals.sort(key= lambda x:x[0])
     res = [] # created an empty list 
     for interval in intervals:
         if not res or res[-1][1] < interval[0]:
             res.append(interval)
         else:
             res[-1][1] = max(interval[1], res[-1][1])
     return res 

     #TC: O(nlogn) sort invocation, we do a simple linear scan of the list
     #SC: O(n) 
# @lc code=end

