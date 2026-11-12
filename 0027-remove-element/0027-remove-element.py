class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_idx = 0

        for num in nums:
            if num != val:
                nums[write_idx] = num
                write_idx += 1

        return write_idx