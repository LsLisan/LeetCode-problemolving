class Solution(object):
    def isHappy(self, n):
        seen = {2,4,37}
        while (n!=1 and n not in seen):
            seen.add(n)
            total = 0

            while n>0:
                digit = n% 10
                total = total+ (digit**2)
                n= n//10
            n=total

        return n==1 

                    