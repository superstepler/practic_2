class Train:
    def __init__(self, destination_point, train_number, departure_time):
        self.destination_point = destination_point
        self.train_number = train_number
        self.departure_time = departure_time

    def set_destination_point(self, destination_point):
        self.destination_point = destination_point
    def set_train_number(self, train_number):
        self.train_number = train_number
    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
    def __str__(self):
        return f"Destination_point: {self.destination_point}, Train_number: {self.train_number}, Departure_time: {self.departure_time} "

trains = [Train("Tomsk", "801-850", "17:45"),
         Train("Moskov", "851-898", "20:15"),
         Train("Omsk", "601-698", "14:30")]

def train_search(trains):
    search_num = input("Enter the number train: ")
    for train in trains:
        if train.train_number == search_num:
            return train

found_train = train_search(trains)
print(f"found_train: {found_train}")
