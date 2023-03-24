"""
1480. Running Sum of 1d Array
Easy

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
from typing import List


def runningSum(nums: List[int]) -> List[int]:
        ans = [] # empty list to store the running sums
        tmp = 0 # temporary variable to store the running sum
        for val in nums: # iterate through the list
            tmp = val+tmp # add the current value to the running sum
            ans.append(tmp) # append the running sum to the list
        return ans

def test_runningSum():
    assert runningSum([1,2,3,4]) == [1,3,6,10], "Should be [1,3,6,10]"
    assert runningSum([1,1,1,1,1]) == [1,2,3,4,5], "Should be [1,2,3,4,5]"
    assert runningSum([3,1,2,10,1]) == [3,4,6,16,17], "Should be [3,4,6,16,17]"

if __name__ == "__main__":
    test_runningSum()
    print("Everything passed")

"""
time complexity: O(n)
    - iterates through the list once so the time is proportional to the length of the list
    - got a run time of 40 ms, which beats 73.61% of users


space complexity: O(n)
    - creates a new list that is the same length as the input list
    - got a memory usage of 14.1 MB, which beats 18.55% of users
"""
