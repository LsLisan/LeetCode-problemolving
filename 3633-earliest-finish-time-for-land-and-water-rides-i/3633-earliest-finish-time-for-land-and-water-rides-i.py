class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        n = len(landStartTime)
        m = len(waterStartTime)

        minLandEnd = float('inf')
        for i in range(n):
            minLandEnd = min(
                minLandEnd,
                landStartTime[i] + landDuration[i]
            )

        minWaterEnd = float('inf')
        for j in range(m):
            minWaterEnd = min(
                minWaterEnd,
                waterStartTime[j] + waterDuration[j]
            )

        answer = float('inf')

        for j in range(m):
            finishTime = (
                max(minLandEnd, waterStartTime[j])
                + waterDuration[j]
            )
            answer = min(answer, finishTime)

        for i in range(n):
            finishTime = (
                max(minWaterEnd, landStartTime[i])
                + landDuration[i]
            )
            answer = min(answer, finishTime)

        return answer