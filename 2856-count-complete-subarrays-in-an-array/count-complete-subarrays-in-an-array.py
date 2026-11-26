class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        left = 0
        freq = {}
        count = 0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while len(freq) == k: 
                freq[nums[left]] = freq.get(nums[left], 0) - 1
                if not freq[nums[left]]:
                    del freq[nums[left]]
                left += 1
                count += len(nums) - right
        return count