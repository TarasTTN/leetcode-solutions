class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            h_left = height[left]
            h_right = height[right]

            current_water = width * min(h_left, h_right)
            if current_water > max_water:
                max_water = current_water

            if h_left < h_right:
                left += 1
            else:
                right -= 1

        return max_water