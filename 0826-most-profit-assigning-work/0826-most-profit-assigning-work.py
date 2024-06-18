class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        profitnew = sorted(profit, reverse=True)
        helper = {} #contains the least difficulty for each profit
        for i in range(len(profit)):
            helper.setdefault(profit[i], difficulty[i])
            if difficulty[i]<helper[profit[i]]:
                helper[profit[i]] = difficulty[i]
        j = 0
        for i in sorted(worker, reverse=True):
            while j < len(profit):
                if i>=helper[profitnew[j]]:
                    ans += profitnew[j]
                    break
                else:
                    j += 1
        return ans
		