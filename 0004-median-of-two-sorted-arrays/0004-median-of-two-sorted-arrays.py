class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while True:
            i = (left + right) // 2
            j = half - i  

            a_left = nums1[i - 1] if i > 0 else float("-infinity")
            a_right = nums1[i] if i < m else float("infinity")

            b_left = nums2[j - 1] if j > 0 else float("-infinity")
            b_right = nums2[j] if j < n else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2 != 0:
                    return float(min(a_right, b_right))
                return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1