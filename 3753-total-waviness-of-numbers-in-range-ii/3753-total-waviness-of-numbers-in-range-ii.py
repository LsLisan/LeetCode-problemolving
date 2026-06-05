class Solution(object):
    def totalWaviness(self, num1, num2):

        def solve(n):
            if n < 0:
                return 0

            s = str(n)
            digits = [int(c) for c in s]
            m = len(digits)

            memo = {}

            def dp(pos, tight, started, prev2, prev1):
                key = (pos, tight, started, prev2, prev1)

                if not tight and key in memo:
                    return memo[key]

                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9
                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if started == 0:
                        if d == 0:
                            cnt, wav = dp(pos + 1, ntight, 0, 0, 0)
                        else:
                            cnt, wav = dp(pos + 1, ntight, 1, -1, d)

                    elif started == 1:
                        cnt, wav = dp(pos + 1, ntight, 2, prev1, d)

                    else:
                        add = 0
                        if (prev1 > prev2 and prev1 > d) or \
                           (prev1 < prev2 and prev1 < d):
                            add = 1

                        cnt, wav = dp(pos + 1, ntight, 2, prev1, d)
                        wav += add * cnt

                    total_count += cnt
                    total_waviness += wav

                res = (total_count, total_waviness)

                if not tight:
                    memo[key] = res

                return res

            return dp(0, True, 0, 0, 0)[1]

        return solve(num2) - solve(num1 - 1)