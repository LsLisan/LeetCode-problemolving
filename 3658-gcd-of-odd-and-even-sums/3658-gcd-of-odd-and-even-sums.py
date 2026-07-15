class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        sumOdd = n*n
        sumEven = n*(n+1)

        return gcd(sumOdd,sumEven)