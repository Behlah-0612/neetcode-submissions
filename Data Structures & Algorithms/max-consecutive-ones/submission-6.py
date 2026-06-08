class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0

        for i in range(len(nums)):
            ans = 0
            for j in range(i,len(nums)):
                if nums[j] == 0:
                    break
                ans += 1
            answer = max(answer, ans)

        return answer
