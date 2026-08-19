class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            if 2 <= s <= 9:
                rows[r] = rows.get(r, 0) | (1 << s)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = (mask & 0b0000111100) == 0
            mid = (mask & 0b0011110000) == 0
            right = (mask & 0b1111000000) == 0

            if left and right:
                ans += 2
            elif left or mid or right:
                ans += 1

        return ans
