
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        element = None
        for i in range(n):
            if cnt == 0:
                cnt = 1
                element = nums[i]
            elif element == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        
        cnt1 = 0

        for i in range(n):
            if nums[i] == element:
                cnt1 += 1
        
        if cnt1 > (n//2):
            return element
        return -1
            
        


            

