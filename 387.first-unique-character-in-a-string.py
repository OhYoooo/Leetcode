import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(list(s))
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1
