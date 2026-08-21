class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        highest = 0
        while left <= right:
            if heights[left] < heights[right]:
                width = right - left
                height = min(heights[left],heights[right])
                area = width * height
                left += 1
            else:
                width = right - left
                height = min(heights[left],heights[right])
                area = width * height
                right -= 1
            if area > highest:
                highest = area
        return highest
            
            

