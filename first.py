# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

def every_second_to_new_list(input_list):
    if type(input_list) != list:
        raise TypeError('Input is not a list.')
    else:
        output = []
        for i in range(len(input_list)):
            if i%2 is 1:
                output.append(input_list[i])
        return output

testlist = [1, 2, 3, 4, 5]

print(every_second_to_new_list(testlist))
print(every_second_to_new_list("apple"))
