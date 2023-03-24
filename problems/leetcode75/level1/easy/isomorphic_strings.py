"""
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        id = 0 # id to assign to each character
        ids = {} # dictionary to store the character and its id
        s_id = '' # string to store the id of each character in s
        for char in s: # iterate through s
            if char in ids: # if the character is already in the dictionary
                s_id = s_id + str(ids[char]) + '-' # add the id to the string
            else: # if the character is not in the dictionary
                ids[char] = id # add the character and its id to the dictionary
                s_id = s_id + str(ids[char]) + '-' # add the id to the string
                id += 1 # increment the id

        # repeat the same process for t
        id = 0
        ids = {}
        t_id = ''
        for char in t:
            if char in ids:
                t_id = t_id + str(ids[char]) + '-'
            else:
                ids[char] = id
                t_id = t_id + str(ids[char]) + '-'
                id += 1
        return s_id == t_id # return True if the strings are isomorphic
    # time complexity: O(n)
    #     - iterates through the list once so the time is proportional to the length of the list
    #     - technically it runs through the string twice, but the time complexity is still O(n)

    # space complexity: O(n)
    #     - creates a new list that is the same length as the input list   


    def isIsomorphic(self, s, t):
        if len(s) != len(t): # if the strings are not the same length, they cannot be isomorphic
            return False

        n = len(s) # get the length of the string
        s_ids, t_ids = [-1] * 256, [-1] * 256 # create two lists to store the ids of each character

        for i in range(n): # iterate through the strings
            s_char, t_char = ord(s[i]), ord(t[i]) # get the ascii code for the characters at the current index
            if s_ids[s_char] != t_ids[t_char]: # if the ids are not the same (if the character is new, itll be a -1. if not, itll be a matching index)
                return False
            s_ids[s_char], t_ids[t_char] = i, i # assign the current index to the character's id
        return True
    # time complexity: O(n)
    #     - iterates through the list once so the time is proportional to the length of the list
    #     - actually only runs once so its better than the above solution

    # space complexity: O(1)
    #    - creates a new list of a fixed length for each string, so the space used doesn't change with input size

def test_isIsomorphic():
    assert Solution().isIsomorphic('egg', 'add') == True, "Should be True"
    assert Solution().isIsomorphic('foo', 'bar') == False, "Should be False"
    assert Solution().isIsomorphic('paper', 'title') == True, "Should be True"
    assert Solution().isIsomorphic('ab', 'aa') == False, "Should be False"

if __name__ == "__main__":
    test_isIsomorphic()
    print("Everything passed")