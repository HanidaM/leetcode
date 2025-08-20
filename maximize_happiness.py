class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        hpy_sum = 0

        for i in range(k):
            cur_happy = max(0, happiness[i] - i)
            hpy_sum += cur_happy

        return hpy_sum


