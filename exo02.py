# Practice 02 - Python basics
# The program ask the user to enter a number
# then calculate the sum from 1 to that number


# Let's define a function that calculates the sum from number 1 to a number 2
def calculate_sum(num1, num2):
    """Returns the sum from number 1 to a number 2"""

    result = 0
    for n in range(num1, num2 + 1):
        result = result + n

    return result


# Let's define a function that prints the sum operations from number 1 to a number 2
def print_calculate_sum(num1, num2):
    """Prints the operation line of the sum from number 1 to a number 2"""

    for n in range(num1, num2 + 1):
        if n == num2:
            print(str(n) + " = ", end='')
        else:
            print(str(n) + " + ", end='')


def exo02():

    while True:

        # Catch with the try the possible exceptions that user can enter
        try:
            # Capture the user input
            n = int(input("Enter a number : "))

        # First exception if the user enter a value that is not integer
        except ValueError:
            print("\n!! Error : please enter an integer. !! \n")

        # Second exception if the user quit the program with Ctrl+Z or Ctrl+C
        except (EOFError, KeyboardInterrupt):
            print("\nBYE BYE \n")
            break

        # If no exception, let's print the operations and the result
        # like this : 1 + 2 + ... + n = result
        else:
            if n < 2:
                print("Please enter a number > 1 \n")
            else:
                print_calculate_sum(1, n)
                print(str(calculate_sum(1, n)))


if __name__ == "__main__":
    exo02()
