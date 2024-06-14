class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        seen=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<=seen:
                res=res+abs(seen+1-nums[i])
                nums[i]=seen+1
            seen=nums[i]
        return res
        