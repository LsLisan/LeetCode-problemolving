class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        digits = [ch for ch in s if ch != '0']
        
        if not digits:
            return 0
        
        x = int("".join(digits))
        digit_sum = sum(int(ch) for ch in digits)
        
        return x * digit_sum