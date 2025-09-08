class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stacked = []
        for p, s in pairs:
            stacked.append((target - p) / s)
            if len(stacked) >= 2 and stacked[-1] <= stacked[-2]:
                stacked.pop()
        return len(stacked)
