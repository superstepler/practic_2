class Numbers:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def output(self):
        print(f"Numebr 1: {self.number_1}, Number_2: {self.number_2}")


    def number_change(self, new_num1, new_num2):
        self.new_num1 = new_num1
        self.new_num2 = new_num2

    def sum_num(self):
        return self.number_1 + self.number_2

    def max_num(self):
        return max(self.number_1, self.number_2)

numbers = Numbers(15,30)
while True:
    choice = (input("1 - initial numbers, 2 - new numbers, 3 - Exit"))
    if choice == "1":
        numbers.output()
        print("Sum:", numbers.sum_num())
        print("Max:", numbers.max_num())
    elif choice == "2":
        new_num1 = int(input("Enter new number 1: "))
        new_num2 = int(input("Enter new number 2: "))
        new_num = Numbers(new_num1, new_num2)
        new_num.output()
        print("Sum:", new_num.sum_num())
        print("Max:", new_num.max_num())
    elif choice == "3":
        break