class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:

                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return ans
