from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1
        sorted_nums = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        result = [num for num, freq in sorted_nums[:k]]
        return result
## TODO unsolved 