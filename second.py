# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def write_to_file_ten_times(file_name, input_string):
    try:
        if type(input_string) != str:
            raise TypeError('Input is not a string')
        else:
            f = open(file_name, 'w')
            f.write(input_string * 10)
            f.close
            return True
    except:
        return False

print(write_to_file_ten_times("tree.txt", "apple"))
