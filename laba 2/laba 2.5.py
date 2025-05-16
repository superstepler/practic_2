class Class:
    def __init__(self, value_1=0, value_2=1):
        self.value_1 = value_1
        self.value_2 = value_2
    def __del__(self):
        print(f"Object deleted")

while True:
    object = input("Create the object? (Yes/No): ").lower()
    if object == "yes":
        creat = Class()
        print("Objert creat")
        break
    elif object == "no":
        print("Object is not created")
        break
    else:
        print("Error")