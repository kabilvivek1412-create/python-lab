class ParkingQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, car):
        if len(self.queue) == self.size:
            print("Parking Full! Cannot park", car)
        else:
            self.queue.append(car)
            print(car, "entered the parking.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Parking Empty! No cars to remove.")
        else:
            car = self.queue.pop(0)
            print(car, "left the parking.")

    def display(self):
        if len(self.queue) == 0:
            print("Parking is empty.")
        else:
            print("Cars in Parking:")
            for car in self.queue:
                print(car)


size = int(input("Enter parking capacity: "))                                                                            
parking = ParkingQueue(size)

while True:
    print("\n--- Car Parking System ---")
    print("1. Car Entry (Enqueue)")
    print("2. Car Exit (Dequeue)")
    print("3. Display Parked Cars")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        car = input("Enter Car Number: ")
        parking.enqueue(car)

    elif choice == 2:
        parking.dequeue()

    elif choice == 3:
        parking.display()

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
