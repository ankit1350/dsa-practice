class Solution:
    def longestSubarray(self, nums, k):
        mp = {}              # prefix_sum : first_index
        curr_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_sum += num

            # Case 1: subarray from 0 to i
            if curr_sum == k:
                max_len = i + 1

            # Case 2: subarray exists in between
            if curr_sum - k in mp:
                length = i - mp[curr_sum - k]
                max_len = max(max_len, length)

            # store first occurrence only
            if curr_sum not in mp:
                mp[curr_sum] = i

        return max_len
