#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary 
        hashmap = {}
        #target - nums[i] 找出补数
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
    # TC： O（n)  SC: O(n)
# @lc code=end

