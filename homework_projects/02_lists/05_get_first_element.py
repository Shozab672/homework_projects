## Problem Statement

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# ## Starter Code

def main():
    print("lst as a parameter and prints the first element in the list! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()


## Solution


def get_first_element(lst):
    """
    Prints the first element of a provided list. Assumes the list is non-empty.
    """
    if lst:  # Ensure the list is not empty
        print(f"The first element is: {lst[0]}")
    else:
        print("The list is empty. No first element to display.")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    while True:
        elem = input("Please enter an element of the list or press Enter to stop: ").strip()
        if elem == "":
            break  # Stop when user presses Enter without providing input
        lst.append(elem)
    return lst

def main():
    print("Build your list by entering elements one at a time. Press Enter on an empty input to stop.")
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
