class Solution:
    def merge_arrays(self, nums1: list[int], nums2: list[int], m, n) -> list[int]:
        nums3 = [None] * (m + n)

        i = j = k = 0

        # Traverse both arrays
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i+=1
                k+=1
            else:
                nums3[k] = nums2[j]
                j+=1
                k+=1

        # check of any element is left
        while i < m:
            nums3[k] = nums1[i]
            i+=1
            k+=1

        while j < n:
            nums3[k] = nums2[j]
            j+=1
            k+=1

        return nums3

    def find_median(self, nums: list[int]) -> float:
        median = None

        # length of the array
        length = len(nums)

        # check parity of the array
        if length % 2 != 0:
            median = nums[length // 2]
        else:
            first = nums[length // 2 - 1]
            print(f"first = {first}")
            second = nums[length // 2]
            print(f"second = {second}")
            median = (first + second) / 2

        return median


    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # merge two arrays
        nums3 = self.merge_arrays(nums1, nums2, len(nums1), len(nums2))
        # calculate the median
        return self.find_median(nums3)

solution = Solution()
median = solution.findMedianSortedArrays([0,0], [0,0])
print(median)
