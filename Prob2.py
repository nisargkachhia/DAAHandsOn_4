# Problem 2: Remove duplicates from a sorted array
def remove_duplicates(array):
    if not array:
        return array
    
    # Pointer for the position of the next unique element
    index = 1
    
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            array[index] = array[i]
            index += 1
    
    # Slice the array to only include unique elements
    return array[:index]

if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter a sorted array: ")
    
    # Convert input string to a list of integers
    array = list(map(int, user_input.split()))
    
    # Sort the array to make sure it's sorted (in case the user inputs unsorted data)
    array.sort()
    
    # Print original array
    print("Original array (sorted): ", array)
    
    # Remove duplicates
    unique_array = remove_duplicates(array)
    
    # Print the array after removing duplicates
    print("Array after removing the duplicate elements: ", unique_array)
