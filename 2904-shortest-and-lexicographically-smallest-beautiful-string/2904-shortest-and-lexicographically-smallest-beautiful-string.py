class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        left = 0
        ones = 0
        min_len = n + 1
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                while left <= right and s[left] == '0':
                    left += 1

                curr_len = right - left + 1
                curr = s[left:right + 1]

                if curr_len < min_len:
                    min_len = curr_len
                    ans = curr
                elif curr_len == min_len and (not ans or curr < ans):
                    ans = curr

        return ans
