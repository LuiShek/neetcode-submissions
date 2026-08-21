class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        stack = []  # indices, heights strictly decreasing
        water = 0

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                distance = i - left - 1
                bounded_height = min(height[i], height[left]) - height[top]
                water += distance * bounded_height
            stack.append(i)

        return water