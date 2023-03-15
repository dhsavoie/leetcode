"""
724. Find Pivot Index
Easy

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""

from typing import List

def pivotIndex(self, nums: List[int]) -> int:
    leftsum, rightsum = 0, sum(nums) # initialize leftsum and rightsum to 0 and the sum of the list respectively
    for i in range(len(nums)): # iterate through the list
        rightsum -= nums[i] # subtract the current value from the rightsum
        if rightsum == leftsum: # if the leftsum and rightsum are equal, return the index
            return i
        else: # otherwise, add the current value to the leftsum
            leftsum += nums[i]
    return -1

def test_pivotIndex():
    assert pivotIndex([1,7,3,6,5,6]) == 3, "Should be 3"
    assert pivotIndex([1,2,3]) == -1, "Should be -1"
    assert pivotIndex([2,1,-1]) == 0, "Should be 0"

if __name__ == "__main__":
    test_pivotIndex()
    print("Everything passed")

"""
time complexity: O(n)
    - iterates through the list once so the time is proportional to the length of the list
    - got a run time of 133 ms, which beats 99.83% of users

space complexity: O(1)
    - only creates two variables to store the leftsum and rightsum
    - got a memory usage of 15.3 MB, which beats 37.34% of users

"""