class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        mx_amount = 0
        while (left != right):
            if heights[left] == 0: 
                left += 1
                continue
            elif heights[right] == 0:
                right -= 1
                continue
            mx_amount = max(mx_amount,(right - left) * min(heights[right],heights[left]))

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return mx_amount