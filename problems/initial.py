def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")


"""
the format for all of these problems will pretty much be exactly this

first you will have a function that will be called by the test function

then you will have the test function that will call the function and assert that the function returns the correct value

then you will have the if __name__ == "__main__": block that will call the test function and print out a message if the test passes

then finally at the bottom i'll have some notes on the problem, like time complexity, space complexity, and any other notes i think are important

"""