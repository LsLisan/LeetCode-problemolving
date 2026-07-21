class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        base = s.count('1')
        t = "1" + s + "1"
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        ans = base

        for k in range(1, len(runs) - 1):
            if runs[k][0] == '1':
                left_zero = runs[k - 1]
                right_zero = runs[k + 1]
                if left_zero[0] == '0' and right_zero[0] == '0':
                    gain = left_zero[1] + right_zero[1]
                    ans = max(ans, base + gain)

        return ans
