from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        idx = [0] * (n + 1)

        digits = []
        prefSum = [0]

        for i, ch in enumerate(s):
            idx[i] = len(digits)
            if ch != '0':
                d = ord(ch) - 48
                digits.append(d)
                prefSum.append(prefSum[-1] + d)
        idx[n] = len(digits)

        m = len(digits)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefNum[i] = number formed by first i non-zero digits
        prefNum = [0] * (m + 1)
        for i in range(m):
            prefNum[i + 1] = (prefNum[i] * 10 + digits[i]) % MOD

        ans = []

        for l, r in queries:
            L = idx[l]
            R = idx[r + 1]

            length = R - L

            x = (prefNum[R] - prefNum[L] * pow10[length]) % MOD
            digitSum = prefSum[R] - prefSum[L]

            ans.append((x * digitSum) % MOD)

        return ans