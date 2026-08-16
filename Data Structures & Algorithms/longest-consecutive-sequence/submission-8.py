class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        c = 1
        longest = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                c += 1
                longest = max(longest, c)

            elif nums[i + 1] - nums[i] == 0:
                continue

            else:
                c = 1

        return longest