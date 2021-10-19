class Solution:
    def merge_arrays(self, nums1: list[int], nums2: list[int], m, n) -> list[int]:
        nums3 = [None] * (m + n)

        i = j = k = 0

        # Traverse both arrays
        while i < m and j < n:
            if nums[i] < nums[j]:
                nums3[k] = nums[i]
                i+=1
                k+=1
            else:
                nums3[k] = nums[j]
                j+=1
                k+=1
                


    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        pass

solution = Solution()
solution.findMedianSortedArrays([1,2,3], [4,5,6])
