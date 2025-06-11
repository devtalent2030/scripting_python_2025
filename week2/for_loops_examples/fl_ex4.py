# Example 4: Nested for loops

# Loop to print column headings.
for column in range(1, 6): 
    print(str(column), end="\t")
print("\n")

# Start of outer loop: a die size on each row.
for row in range(4, 12, 2):
    # Print the die size at the start of each row.
    print("\n" + str(row), end="\t")
  
    # Start inner loop used for hit point values.
    for column in range(1, 6):
        # Determine and print the hit point values.
        print(str(int((row/2+1)*column+(row/2-1))), end="\t")
        # End of the inner loop (columns).
    # End of outer loop (rows).
