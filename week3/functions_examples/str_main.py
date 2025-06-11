"""
This script will utilize the str_util_module.
"""

# Import the str_util_module
import str_util_module as str_util

if __name__ == "__main__":
    # Example usage of the functions in str_util_module
    str1 = "Hello"
    str2 = "World"
    
    # Concatenate two strings
    result = str_util.concat_str(str1, str2)
    print(f"Concatenated string: {result}")
    
    # Concatenate multiple strings
    result = str_util.concat_many("Hello", " ", "World", "!")
    print(f"Concatenated many strings: {result}")
    
    # Concatenate a list of strings
    str_list = ["Hello", " ", "World", "!"]
    result = str_util.concat_list(str_list)
    print(f"Concatenated list of strings: {result}")
    
    # Concatenate a list of strings with a separator
    str_list2 = ["Hello", "how", "are", "you"]
    sep = "-"
    result = str_util.concat_list_with_sep(str_list2, sep)
    print(f"Concatenated list with separator: {result}")