class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        ps = [-1] * n
        ns = [n] * n

        stack = []

        # Previous Smaller Index
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                ps[i] = stack[-1]

            stack.append(i)

        stack = []

        # Next Smaller Index
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                ns[i] = stack[-1]

            stack.append(i)

        ans = 0

        for i in range(n):
            width = ns[i] - ps[i] - 1
            area = heights[i] * width
            ans = max(ans, area)

        return ans