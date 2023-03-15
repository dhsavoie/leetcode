"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List

def twoSum1(self, nums: List[int], target: int) -> List[int]:
    # this was the first attempt, this is a brute force attempt
    for i in range(len(nums)): # iterate through the list
        for n in range(i+1, len(nums)): # iterate through the list again for each number in the first iteration
            if nums[i] + nums[n] == target: # if the two numbers add up to the target, return the indices
                return [i, n]

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # this is the second attempt, this is a more efficient attempt, using hashmaps
    d = {}
    for idx, value in enumerate(nums):
        if (target - value) in d:
            return [d[target-value], idx]
        else:
            d[value] = idx

def test_twoSum():
    assert twoSum([2,7,11,15], 9) == [0,1], "Should be [0,1]"
    assert twoSum([3,2,4], 6) == [1,2], "Should be [1,2]"
    assert twoSum([3,3], 6) == [0,1], "Should be [0,1]"

if __name__ == "__main__":
    test_twoSum()
    print("Everything passed")

"""
time complexity: O(n)
    - iterates through the list once so the time is proportional to the length of the list
    - got a run time of 60 ms, which beats 84.21% of users

space complexity: O(n)
    - creates a dictionary to store the values and indices of the list
    - got a memory usage of 15.3 MB, which beats 16.58% of users

The first attempt here was a brute force algorithm and it iterates through the list once for every element in the list
This gives it a time complexity of O(n^2)

The second attempt here creates a dictionary to store the values and indices of the list and 
checks if the target minus the current value is in the dictionary already. It is only iterating through the list once,
and it uses the 'in' keyword, which for some data structures (such as sets and dictionaries) is O(1) and 
for others (like lists or tuples) is O(n). In this case we use it on a dictionary so it is O(1), meaning the overall
time complexity is O(n) because of just the list iteration used to create the dictionary.


"""