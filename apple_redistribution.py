class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)

        total_apples = sum(apple)
        boxes_used = 0

        for cap in capacity:
            if total_apples <= 0:
                break
            total_apples -= cap
            boxes_used += 1

        return boxes_used
