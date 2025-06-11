"""
This module contains the main function to demonstrate the Person class functionality.
"""
# Import the Person class from the person module
# person represents the file name or module name 
# Person represents the class name 
# (Take a note of the lowercase 'p' in person and uppercase 'P' in Person)
from person import Person

def main():
    """
    Main function to demonstrate the Person class functionality.
    This function creates a Person object and prints its information.
    """
    # Create a Person object
    person = Person(name="Alice", age=30, height=165.5, weight=60.0, studying=True)

    # Print the person's information
    print(person)

    # Check if the person is studying
    if person.is_studying():
        print(f"{person.get_name()} is currently studying.")
    else:
        print(f"{person.get_name()} is not studying.")

if __name__ == "__main__":
    main()