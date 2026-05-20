class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        C = []

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])

            common = setA.intersection(setB)
            C.append(len(common))

        return C