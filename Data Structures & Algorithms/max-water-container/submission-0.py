class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0
        left, right = 0, len(heights) - 1
        
        while left < right:
            # 1. Calculate the width between the two bars
            width = right - left
            
            # 2. Water height is limited by the shorter of the two bars
            current_water = width * min(heights[left], heights[right])
            
            # 3. Update the maximum water found so far
            max_water = max(max_water, current_water)
            
            # 4. Move the pointer pointing to the shorter bar inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water





        