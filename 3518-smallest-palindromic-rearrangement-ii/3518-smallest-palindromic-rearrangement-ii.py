from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        mid = ""
        cnt = {}

        for c in sorted(freq):
            if freq[c] & 1:
                mid = c
            if freq[c] // 2:
                cnt[c] = freq[c] // 2

        rem = sum(cnt.values())

        fact = [1] * (rem + 1)
        for i in range(1, rem + 1):
            fact[i] = fact[i - 1] * i

        ways = fact[rem]
        for v in cnt.values():
            ways //= fact[v]

        if ways < k:
            return ""

        left = []

        while rem:
            for c in sorted(cnt):
                if cnt[c] == 0:
                    continue

                newWays = ways * cnt[c] // rem

                if newWays < k:
                    k -= newWays
                else:
                    left.append(c)
                    ways = newWays
                    cnt[c] -= 1
                    rem -= 1
                    break

        left = "".join(left)
        return left + mid + left[::-1]
