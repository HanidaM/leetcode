class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = set(nums)
        lngst = 0
        for num in consecutive:
            if num - 1 not in consecutive:
                length = 1
                while num + length in consecutive:
                    length += 1
                lngst = max(lngst, length)
        return lngst