MAX_LENGTH: int = 3  # Define the maximum length of the list

def shorten(lst):
    """
    Removes elements from the end of the list until its length is equal to MAX_LENGTH.
    Prints each removed element. If the list is already shorter than MAX_LENGTH, it remains unchanged.
    """
    print(f"Original list: {lst}")
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"Removed: {last_elem}")
    print(f"Final list (after shortening): {lst}")

def get_lst():
    """
    Prompts the user to enter elements for the list one by one.
    Returns the constructed list.
    """
    lst = []
    while True:
        elem = input("Enter an element for the list (or press Enter to stop): ").strip()
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    """
    Main function that gets a list from the user and passes it to the `shorten` function.
    """
    print(f"Welcome! This program ensures your list is at most {MAX_LENGTH} items long.")
    lst = get_lst()
    if lst:
        shorten(lst)
    else:
        print("The list is empty. Nothing to shorten.")

if __name__ == '__main__':
    main()
