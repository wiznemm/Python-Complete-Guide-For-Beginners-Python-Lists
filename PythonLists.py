#Python lists are ordered collections of items, allowing for versatile data storage and manipulation.

#✅ Create a list

#Creating a list is simple. You enclose elements within square brackets [ ] and separate them with commas. Here's an example:

my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

#You can also create an empty list:

empty_list = []
print(empty_list)  # Output: []

#===============================================================================================================================================

#✅ Create list with different types

#Python lists can contain elements of different data types, allowing for flexibility. Here's an example of a list with mixed types:

mixed_list = [1, "apple", True, 3.14]
print(mixed_list)  # Output: [1, 'apple', True, 3.14]

#===============================================================================================================================================

#✅ Select the valid list

#When creating lists, ensure they follow the correct syntax by enclosing elements within square brackets [ ]. Here's a valid list:

valid_list = [1, 2, 3, 4, 5]
print(valid_list)  # Output: [1, 2, 3, 4, 5]

#===============================================================================================================================================

#✅ List of lists

#Lists can also contain other lists, creating a nested structure. This is useful for representing hierarchical or multi-dimensional data. Here's an example:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#===============================================================================================================================================

#🔍 Subsetting Lists

#Subsetting allows you to access specific elements or slices of elements from a list.

#✅ Subset and conquer

#You can access individual elements of a list by their index. Remember, Python uses zero-based indexing. Here's an example:

my_list = [1, 2, 3, 4, 5]
element = my_list[0]  # Access the first element
print(element)  # Output: 1

#You can also use negative indices to access elements from the end of the list. -1 refers to the last element, -2 refers to the second last, and so on.

#===============================================================================================================================================

#✅ Subset and calculate

#Subsetting can be combined with calculations or operations on specific subsets of data. For example, calculating the sum of the first three elements:

my_list = [1, 2, 3, 4, 5]
sum_subset = sum(my_list[:3])  # Calculate the sum of the first three elements
print(sum_subset)  # Output: 6

#===============================================================================================================================================

#🔍 Slicing and dicing

#Slicing allows you to extract portions of a list by specifying a range of indices.

#✅ Slicing and dicing

#You can specify a start index and an end index separated by a colon : to slice a list. Here's an example:

my_list = [1, 2, 3, 4, 5]
subset = my_list[1:4]  # Extract elements from index 1 to 3 (exclusive)
print(subset)  # Output: [2, 3, 4]

#===============================================================================================================================================

#✅ Slicing and dicing (2)

#Slicing can also include a step value, which determines the interval between elements to be included in the slice. Here's an example:

my_list = [1, 2, 3, 4, 5]
subset = my_list[::2]  # Extract every second element
print(subset)  # Output: [1, 3, 5]

#===============================================================================================================================================

#✅ Subsetting lists of lists

#Nested lists can be subsetted by chaining multiple index operations. Here's an example:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = nested_list[1][2]  # Access the element at row 1, column 2
print(element)  # Output: 6

#===============================================================================================================================================

#🔧 Manipulating Lists

#Python lists support various methods for modifying and manipulating their contents.

#✅ Replace list elements

#You can replace elements within a list by assigning new values to specific indices. Here's an example:

my_list = [1, 2, 3, 4, 5]
my_list[2] = 10  # Replace the third element with 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

#===============================================================================================================================================

#✅ Extend a list

#Appending or extending lists allows you to add new elements to the end of an existing list. Here's how you can extend a list:

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # Extend the list with additional elements
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

#You can also use the + operator to concatenate lists:

my_list = [1, 2, 3]
new_elements = [4, 5, 6]
concatenated_list = my_list + new_elements
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

#===============================================================================================================================================

#✅ Delete list elements

#Deleting elements from a list can be done using the del statement or the remove() method. Here are examples of both:

#Using del:

my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Delete the third element
print(my_list)  # Output: [1, 2, 4, 5]

#Using remove():

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # Remove the element with value 3
print(my_list)  # Output: [1, 2, 4, 5]

#===============================================================================================================================================
#===============================================================================================================================================

#✅ Inner workings of lists

#Understanding how lists work internally can help you make informed decisions about their usage and performance characteristics.

#In Python, lists are implemented as dynamic arrays, allowing for efficient insertion, deletion, and access of elements. However, resizing the array may incur overhead when the capacity is exceeded, resulting in occasional memory reallocation.

#Additionally, lists support various methods and operations for manipulating their contents, such as sorting, reversing, and searching for elements.

#By understanding these inner workings, you can leverage lists effectively in your Python programs while optimizing performance and memory usage.

#Congratulations on mastering Python lists! 🎉 Now, armed with this knowledge, you're ready to tackle a wide range of data manipulation tasks in Python with confidence.

#===============================================================================================================================================
#===============================================================================================================================================