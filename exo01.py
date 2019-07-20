# Practice 01 - Python basics
# The program ask the user to enter a number
# then tell us if the number is pair or impair


def exo01():

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

        # If no exception, let's print the result
        else:
            # using the modulo operator % to know if the number is pair or impair
            if n % 2 == 0:
                print("\n" + str(n) + " >>> Pair \n")
            else:
                print("\n" + str(n) + " >>> Impair \n")


if __name__ == "__main__":
    exo01()
