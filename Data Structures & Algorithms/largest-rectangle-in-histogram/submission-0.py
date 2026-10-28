class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        max_area = 0
        stack: list[int] = []
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                current_height = heights[stack.pop()]
                left_border = stack[-1] if stack else -1
                area = current_height * (i - 1 - left_border)
                max_area = max(area, max_area)

            stack.append(i)

                

        return max_area