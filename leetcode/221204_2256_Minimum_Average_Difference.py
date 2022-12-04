class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        prefix_sum = [0] * (N+1)
        suffix_sum = [0] * (N+1)
        
        for i in range(N):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        for i in range(N-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + nums[i]
            
        left_avg = 0
        right_avg = 0
        avg_diff = 987654321
        # print(suffix_sum)
        for i in range(N):
            left_avg = prefix_sum[i+1]
            left_avg = left_avg // (i+1)
            
            right_avg = suffix_sum[i+1]
            if i != N - 1:
                right_avg = right_avg // (N - i - 1)
                
            cur_diff = abs(left_avg - right_avg)
            if avg_diff > cur_diff:
                avg_diff = cur_diff
                ans = i                
            
        return ans
                