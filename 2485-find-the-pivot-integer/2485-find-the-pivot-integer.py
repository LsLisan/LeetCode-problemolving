class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot=-1
        leftSum=0
        rightSum=0
        totalSum= n*(n+1)/2
        if (n == 1):
            return n
        for i in range(1,n):
            leftSum = i*(i+1)/2
            rightSum = i+ totalSum- leftSum
            if(leftSum == rightSum):
                pivot = i
                break

        return pivot