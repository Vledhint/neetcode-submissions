class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        # print(f"Valores iniciales de l: {l} y r; {r}")
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            #print(f"Valor de l: {l} , r: {r} en el while")
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            

        return res
