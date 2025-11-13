class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height) - 1
        area = 0
        while l <= r :
            if height[l] < height[r] :
                area = max(area , height[l] * (r-l))
                l += 1
            elif height[l] > height[r]:
                area = max(area , height[r] * (r-l))
                r -= 1
            else :
                area = max(area , height[r] * (r-l))
                l += 1
                r -= 1
        return area