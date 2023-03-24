"""
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    pass

def test_mergeTwoLists():
    assert mergeTwoLists([1,2,4], [1,3,4]) == [1,1,2,3,4,4], "Should be [1,1,2,3,4,4]"
    assert mergeTwoLists([], []) == [], "Should be []"
    assert mergeTwoLists([], [0]) == [0], "Should be [0]"

if __name__ == "__main__":
    test_mergeTwoLists()
    print("Everything passed")
