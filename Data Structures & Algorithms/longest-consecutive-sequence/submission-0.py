class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        set_nums = set(nums)
        mx_k = 0
        for el in set_nums:
            k = 0
            if (el - 1) not in set_nums:
                for i in range(el, el +len(set_nums)):
                    if i in set_nums:
                        k += 1
                    else:
                        break
            mx_k = max(k,mx_k)
        
        return mx_k