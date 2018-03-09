"""
Given an array of integers, return indices of the two numbers such that they add
 up to a specific target.

You may assume that each input would have exactly one solution, and you may not
 use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum(nums, target):
    """
    这种方法多次遍历了nums,时间复杂度是高
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return []

    for index, value in enumerate(nums):
        difference = target - value
        if difference in nums:
            return [index, nums.index(difference)]
    return []


def two_sum_use_dict(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    if len(nums) <= 1:
        return []

    buff_dict = {}
    for index, value in enumerate(nums):
        difference = target - value
        if difference in buff_dict:
            return [buff_dict[difference], index]
        else:
            buff_dict[value] = index
    return buff_dict.values()


if __name__ == "__main__":
    nums = [11, 7, 8, 1, 2]
    target = 9
    result = two_sum(nums, target)
    print(result)
    print(two_sum_use_dict(nums, target))