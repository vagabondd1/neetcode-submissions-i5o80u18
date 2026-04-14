class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        dot_result = 1
        flags = set()
        for index in range(len(nums)):
            if nums[index] == 0:
                flags.add(index)
            else:
                dot_result *= nums[index]

        if len(flags) >= 2: return [0] * len(nums)  
        for index in range(len(nums)):
            if len(flags) > 0:
                if index not in flags:
                    nums[index] = 0
                else:
                    nums[index] = dot_result
            else:
                nums[index] = dot_result // nums[index]
        
        return nums




        
