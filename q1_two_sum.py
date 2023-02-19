from typing import List


class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
    target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.


    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # since we cannot use any element twice, we can use a hashmap
        seen_hashmap = {}  # hashmap of numbers we have seen already

        for i, number in enumerate(nums):
            target_number = target - number  # the number we are looking for in the list
            if target_number in seen_hashmap:
                # since there is only one solution, we can immediately stop
                return [i, seen_hashmap[target_number]]
            seen_hashmap[number] = i  # add the number to the seen hashmap

        # if after finding no solution
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
