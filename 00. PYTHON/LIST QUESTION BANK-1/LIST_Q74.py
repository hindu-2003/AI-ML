# LIST_Q74.py
#74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
#	Original list:	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
#	After packing consecutive duplicates of the said list elements into sublists:
#	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
def dupli_count(input_list):
    result = []
    sublist = [input_list[0]]
    for element in input_list[1:]:
        if element == sublist[-1]:
            sublist.append(element)
        else:
            result.append(sublist)
            sublist = [element]
    result.append(sublist)  # Append the last sublist
    return result
# Main program
original_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
output = dupli_count(original_list)
print(output_list)  # Expected output: [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
