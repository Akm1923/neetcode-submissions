import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        high=len(nums1)-1
        low=0

        mid=(low+high)//2
        if len(nums1)%2==0:
            val=(nums1[mid]+nums1[mid+1])/2
        else:
            val=nums1[mid]
        return val