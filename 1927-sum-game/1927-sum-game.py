class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2

        diff = 0
        q1 = q2 = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < half:
                    q1 += 1
                else:
                    q2 += 1
            else:
                if i < half:
                    diff += int(ch)
                else:
                    diff -= int(ch)

        if q1 == q2:
            return diff != 0

        return abs(diff + 9 * (q1 - q2) / 2.0) > 0