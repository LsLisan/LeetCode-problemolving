class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suf = [0] * (n + 1)
        suf[n] = m

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suf[i] = j + 1

        ans = []
        j = 0
        mismatch_used = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not mismatch_used and suf[i + 1] <= j + 1:
                ans.append(i)
                j += 1
                mismatch_used = True

        return ans if j == m else []