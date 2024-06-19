def pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces for alignment
        for j in range(1, rows - i + 1):
            print(" ", end=" ")

        # Print numbers in ascending order
        for j in range(1, i + 1):
            print(j, end=" ")

        # Print numbers in descending order
        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        # Move to the next line after each row is printed
        print()

# Example usage:
rows = int(input("Enter Number of Rows for Pyramid: "))
pyramid(rows)
