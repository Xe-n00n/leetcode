class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0 
        result = 0
        freqs = {}
        for right in range(len(nums)):
            freqs[nums[right]] = freqs.get(nums[right], 0) + 1
            while max(freqs) - min(freqs) > 2:
                freqs[nums[left]] -= 1
                if not freqs[nums[left]]:
                    del freqs[nums[left]]
                left += 1

            result += right - left + 1 
        return result 