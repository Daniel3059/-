#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using sliding window and hashmap
        if len(s) == 0: # corner case 
            return 0
        i , j = 0, 0
        dic = defaultdict()
        max_len = 0 
        while j < len(s):
            while s[j] in dic :
                del dic[s[i]]
                i += 1
            dic[s[j]] = 1 # j 的字母不在字典里， 更新字典
            max_len = max(max_len, j-i +1)
            j += 1

        return max_len
        


    
    # go through the entire list ,add and remove values from dictionary ,that's very quick operation 
    # TC: O(N) dictionary 
    # SC: O(N)

         
        
# @lc code=end

