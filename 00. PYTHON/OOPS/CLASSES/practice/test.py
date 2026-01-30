
class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, num):
        self.__add_to_result(num)

    def __add_to_result(self, num):
        self.__result += num

    def get_result(self):
        return self.__result

calculator = Calculator()
calculator.add(5)
x = (calculator.get_result())  # Output: 5
print(x)