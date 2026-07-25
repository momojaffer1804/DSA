class Solution:
    def maxProduct(self, n: int) -> int:
        nums = []
        while n :
            last = n % 10
            nums.append(last)
            n = n // 10
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                ans = max(ans , nums[i]*nums[j])
        return ans
        


        