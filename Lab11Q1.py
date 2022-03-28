class Calculator:
    # Creates an instance with two values
    def __init__(self, x, y):
        self.first_num = x
        self.second_num = y

    # Adds input1 + input2
    def adder(self):
        return self.first_num + self.second_num

    # Subtracts input1 - input2
    def subtractor(self):
        # This can also return a negative value
        return self.first_num - self.second_num

    # Multiplies input1 * input2
    def multiplier(self):
        return self.first_num * self.second_num

    # Divides input1 / input2
    def divider(self):
        if self.second_num == 0:
            return "Unable to divide by 0"
        else:
            return self.first_num / self.second_num

    # Clears (requires the user to re-enter)
    def clear(self):
        self.first_num = 0
        self.second_num = 0


def main():
    print("Please add a space between each number")
    first_num, second_num = \
        input("Please enter two numbers: ").split()
    calc = Calculator(int(first_num), int(second_num))
    print(calc.adder())
    print(calc.subtractor())
    print(calc.multiplier())
    print(calc.divider())
    calc.clear()
    # print(calc.adder())
    # print(calc.subtractor())
    # print(calc.multiplier())
    # print(calc.divider())


if __name__ == "__main__":
    main()
