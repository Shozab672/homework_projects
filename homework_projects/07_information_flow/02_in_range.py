## Problem Statement

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high)
#   """
#   Returns True if n is between low and high, inclusive. 
#   high is guaranteed to be greater than low.
#   """

# ## Starter Code


def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()


## Solution


def in_range(n, low, high):

    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:

          return low <= n <= high

def main():
    # Test cases to validate the function
    print(in_range(5, 1, 10))  # True, since 5 is between 1 and 10
    print(in_range(0, 1, 10))  # False, since 0 is less than 1
    print(in_range(10, 1, 10)) # True, since 10 is inclusive in the range
    print(in_range(15, 1, 10)) # False, since 15 is greater than 10

if __name__ == '__main__':
    main()
    
    