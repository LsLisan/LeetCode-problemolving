class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = list(set(nums1) & set(nums2))
        
        if not intersection:
            return -1
        
        return min(intersection)