class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        prefix = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            if cnt[t] > 0:
                cnt[t] -= 1
                prefix.append(target[i])
                continue

            for x in range(t + 1, 26):
                if cnt[x] > 0:
                    cnt[x] -= 1
                    prefix.append(chr(x + ord('a')))

                    ans = ''.join(prefix)
                    for c in range(26):
                        ans += chr(c + ord('a')) * cnt[c]

                    return ans

            break

        while prefix:
            i = len(prefix) - 1

            last = prefix.pop()
            cnt[ord(last) - ord('a')] += 1

            t = ord(target[i]) - ord('a')

            for x in range(t + 1, 26):
                if cnt[x] > 0:
                    cnt[x] -= 1
                    prefix.append(chr(x + ord('a')))

                    ans = ''.join(prefix)

                    for c in range(26):
                        ans += chr(c + ord('a')) * cnt[c]

                    return ans

        return ""
