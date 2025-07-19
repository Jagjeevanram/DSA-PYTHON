class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge and sort
        nums3 = nums1 + nums2
        nums3.sort()

        n = len(nums3)

        if n % 2 == 0:
            # Average of middle two numbers for even length
            median = (nums3[n // 2 - 1] + nums3[n // 2]) / 2
        else:
            # Middle element for odd length
            median = nums3[n // 2]
        
        return median
