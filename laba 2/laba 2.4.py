value_counter = 0
class Counter:
    def __init__(self,value_counter):
        self.value_counter = value_counter

    def augmentation(self):
        self.value_counter += 1

    def decrease(self):
        self.value_counter -= 1

    @property
    def value(self):
        return self.value_counter
counter = Counter(3)
print(f"Value: {counter.value}")
counter.augmentation()
print(f"Аugmentation: {counter.value}")
counter.decrease()
print(f"Decrease: {counter.value}")
