"""
Algorithm:
- Made a Class "CarParkingLot"
    - Initialize a function for "rows columns"
        - Set self.rows = rows
        - Ser self.columns = columns
        - Set self.queue = queue
        - Set self.parking_lot = as a 2D array with dimensions rows x columns, initialized with None values.

    - Initialize a function "park_car"
        - if length of self.queue < self.rows * self.columns
            - add "car" to self.queue
"""

class CarParkingLot:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.queue = []  
        self.parking_lot = [[None for _ in range(columns)] for _ in range(rows)]  # Initialize parking lot grid

    def park_car(self, car):
        if len(self.queue) < self.rows * self.columns:
            self.queue.append(car)
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.parking_lot[i][j] is None:
                        self.parking_lot[i][j] = car
                        print(f"Car {car} parked successfully in row {i + 1}, column {j + 1}.")
                        return
        else:
            print("Parking lot is full. Cannot park the car.")

    def remove_car(self):
        if self.queue:
            removed_car = self.queue.pop(0)
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.parking_lot[i][j] == removed_car:
                        self.parking_lot[i][j] = None
                        print(f"Car {removed_car} removed from the parking lot.")
                        return
        else:
            print("Parking lot is empty. No car to remove.")

    def display_parking_lot(self):
        if not self.queue:
            print("Parking lot is empty.")
            return

        for row in self.parking_lot:
            print(" ".join(str(car) if car is not None else "Empty" for car in row))

# Taking user input for rows and columns
rows = int(input("Enter the number of rows for the parking lot: "))
columns = int(input("Enter the number of columns for the parking lot: "))

# Create parking lot
parking_lot = CarParkingLot(rows, columns)

while True:
    print("\n--- Options ---")
    print("1. Park a car")
    print("2. Remove a car")
    print("3. Display parking lot")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        car_to_park = input("Enter Your Car No. : ")
        parking_lot.park_car(car_to_park)
    elif choice == '2':
        parking_lot.remove_car()
    elif choice == '3':
        parking_lot.display_parking_lot()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
