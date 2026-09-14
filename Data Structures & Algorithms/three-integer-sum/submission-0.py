class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        # Sort the array to use the two-pointer technique
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Target for the other two numbers is -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Sum is too small, make it larger
                elif total > 0:
                    right -= 1  # Sum is too large, make it smaller
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers past the current unique elements
                    left += 1
                    right -= 1
                    
        return res
