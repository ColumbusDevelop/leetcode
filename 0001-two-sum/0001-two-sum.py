class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        previous_nums = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference in previous_nums:
                return (i, previous_nums[n])

            previous_nums[n] = i