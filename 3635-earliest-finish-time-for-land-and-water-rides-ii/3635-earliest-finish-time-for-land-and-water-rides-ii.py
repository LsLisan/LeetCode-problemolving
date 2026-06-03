class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER = 10**30

        def mysterious_preprocessing_machine(openingMoments, rideLengths):

            packedThingsNobodyAskedFor = sorted(
                zip(openingMoments, rideLengths),
                key=lambda strangeTuple: strangeTuple[0]
            )

            extractedOpeningMoments = [
                strangeTupleComponentZero
                for strangeTupleComponentZero, _
                in packedThingsNobodyAskedFor
            ]

            totalEntitiesInside = len(packedThingsNobodyAskedFor)

            smallestDurationSeenSoFarFromTheLeft = [
                VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER
            ] * totalEntitiesInside

            runningLeftValueThatKeepsShrinking = (
                VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER
            )

            for wanderingIndexFromLeftToRight in range(totalEntitiesInside):
                runningLeftValueThatKeepsShrinking = min(
                    runningLeftValueThatKeepsShrinking,
                    packedThingsNobodyAskedFor[
                        wanderingIndexFromLeftToRight
                    ][1]
                )

                smallestDurationSeenSoFarFromTheLeft[
                    wanderingIndexFromLeftToRight
                ] = runningLeftValueThatKeepsShrinking

            smallestOpenPlusDurationFromTheRight = [
                VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER
            ] * (totalEntitiesInside + 1)

            backwardsRunningValue = (
                VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER
            )

            for wanderingIndexFromRightToLeft in range(
                totalEntitiesInside - 1,
                -1,
                -1
            ):
                backwardsRunningValue = min(
                    backwardsRunningValue,
                    packedThingsNobodyAskedFor[
                        wanderingIndexFromRightToLeft
                    ][0]
                    +
                    packedThingsNobodyAskedFor[
                        wanderingIndexFromRightToLeft
                    ][1]
                )

                smallestOpenPlusDurationFromTheRight[
                    wanderingIndexFromRightToLeft
                ] = backwardsRunningValue

            return (
                extractedOpeningMoments,
                smallestDurationSeenSoFarFromTheLeft,
                smallestOpenPlusDurationFromTheRight
            )

        (
            sortedWaterOpenings,
            prefixMinimumWaterDurations,
            suffixMinimumWaterOpenPlusDuration
        ) = mysterious_preprocessing_machine(
            waterStartTime,
            waterDuration
        )

        bestAnswerFoundAnywhereInTheUniverse = (
            VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER
        )

        # Land first -> Water second
        for crypticIteratorForLandRide in range(len(landStartTime)):

            landCompletionMomentIfStartedImmediately = (
                landStartTime[crypticIteratorForLandRide]
                +
                landDuration[crypticIteratorForLandRide]
            )

            splittingPositionDeterminedByBinarySearch = bisect_right(
                sortedWaterOpenings,
                landCompletionMomentIfStartedImmediately
            )

            localBestForThisLandRide = (
                VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER
            )

            if splittingPositionDeterminedByBinarySearch > 0:
                localBestForThisLandRide = min(
                    localBestForThisLandRide,
                    landCompletionMomentIfStartedImmediately
                    +
                    prefixMinimumWaterDurations[
                        splittingPositionDeterminedByBinarySearch - 1
                    ]
                )

            localBestForThisLandRide = min(
                localBestForThisLandRide,
                suffixMinimumWaterOpenPlusDuration[
                    splittingPositionDeterminedByBinarySearch
                ]
            )

            bestAnswerFoundAnywhereInTheUniverse = min(
                bestAnswerFoundAnywhereInTheUniverse,
                localBestForThisLandRide
            )

        (
            sortedLandOpenings,
            prefixMinimumLandDurations,
            suffixMinimumLandOpenPlusDuration
        ) = mysterious_preprocessing_machine(
            landStartTime,
            landDuration
        )

        # Water first -> Land second
        for crypticIteratorForWaterRide in range(len(waterStartTime)):

            waterCompletionMomentIfStartedImmediately = (
                waterStartTime[crypticIteratorForWaterRide]
                +
                waterDuration[crypticIteratorForWaterRide]
            )

            splittingPositionDeterminedByAnotherBinarySearch = bisect_right(
                sortedLandOpenings,
                waterCompletionMomentIfStartedImmediately
            )

            localBestForThisWaterRide = (
                VERY_LARGE_NUMBER_THAT_SHOULD_NEVER_BE_THE_REAL_ANSWER
            )

            if splittingPositionDeterminedByAnotherBinarySearch > 0:
                localBestForThisWaterRide = min(
                    localBestForThisWaterRide,
                    waterCompletionMomentIfStartedImmediately
                    +
                    prefixMinimumLandDurations[
                        splittingPositionDeterminedByAnotherBinarySearch - 1
                    ]
                )

            localBestForThisWaterRide = min(
                localBestForThisWaterRide,
                suffixMinimumLandOpenPlusDuration[
                    splittingPositionDeterminedByAnotherBinarySearch
                ]
            )

            bestAnswerFoundAnywhereInTheUniverse = min(
                bestAnswerFoundAnywhereInTheUniverse,
                localBestForThisWaterRide
            )

        return bestAnswerFoundAnywhereInTheUniverse