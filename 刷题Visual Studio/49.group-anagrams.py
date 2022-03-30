#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        return dic.values()
    
    # TC: O(N KLOGK) N is the length of strs, K is the maximum length of a string in strs.
    # we sort each string in O(klogK) times.
    # SC: O(NK)
# @lc code=end

