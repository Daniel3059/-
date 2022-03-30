#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()
        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False


        # 用BFS
        #TC： O（n^3)
       # SC: O(n)

# @lc code=end

