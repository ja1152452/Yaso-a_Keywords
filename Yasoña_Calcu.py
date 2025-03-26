import os

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, *values):
        self.result = sum(values)
        return self.result

    def subtract(self, *values):
        self.result = values[0]
        for value in values[1:]:
            self.result -= value
        return self.result

    def multiply(self, *values):
        self.result = 1
        for value in values:
            self.result *= value
        return self.result

    def divide(self, *values):
        self.result = values[0]
        try:
            for value in values[1:]:
                if value == 0:
                    raise ValueError("Oops! You can't divide by zero. Please try again.")
                self.result /= value
            return self.result
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def reset(self):
        self.result = 0
        return self.result


def display_menu():
    print("\n=====================")
    print("     CALCULATOR      ")
    print("=====================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset Result")
    print("6. Quit")
    print("=====================")


def main():
    calc = Calculator()
    print("Welcome to the Python Calculator!")

    while True:
        display_menu()

        try:
            choice = int(input("Please choose an option (1-6): ").strip())

            if choice == 1:
                values = input("Enter the numbers to add (separated by spaces): ").strip().split()
                values = [float(value) for value in values]
                result = calc.add(*values)
                print(f"Adding {values}... Your new result is {result}.")
            elif choice == 2:
                values = input("Enter the numbers to subtract (separated by spaces): ").strip().split()
                values = [float(value) for value in values]
                result = calc.subtract(*values)
                print(f"Subtracting {values}... Your new result is {result}.")
            elif choice == 3:
                values = input("Enter the numbers to multiply (separated by spaces): ").strip().split()
                values = [float(value) for value in values]
                result = calc.multiply(*values)
                print(f"Multiplying {values}... Your new result is {result}.")
            elif choice == 4:
                values = input("Enter the numbers to divide (separated by spaces): ").strip().split()
                values = [float(value) for value in values]
                result = calc.divide(*values)
                if result is not None:
                    print(f"Dividing {values}... Your new result is {result}.")
            elif choice == 5:
                result = calc.reset()
                print(f"The result has been reset to {result}.")
            elif choice == 6:
                print(f"Thanks for using the calculator!")
                break
            else:
                print("Invalid option. Please choose a valid menu number.")
        except ValueError:
            print("Oops! Please enter a valid number.")
        finally:
            print("\nOperation completed. Ready for the next one!")
            input("Press Enter to continue...")  # Keeps the user on the same screen


if __name__ == "__main__":
    main()
