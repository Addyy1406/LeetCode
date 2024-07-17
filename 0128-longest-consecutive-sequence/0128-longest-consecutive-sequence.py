class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        lastsmaller = float('inf')
        cnt = 0
        longest = 1

        for i in range(n):
            if nums[i] - 1 == lastsmaller:
                cnt += 1
                lastsmaller = nums[i]
            elif nums[i] != lastsmaller:
                cnt = 1
                lastsmaller = nums[i]
            longest = max(longest, cnt)
        return longest 