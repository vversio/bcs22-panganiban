import time

elevator = ["Ground Floor", "1st Floor", "2nd Floor", "3rd Floor",
            "4th Floor", "5th floor", "6th Floor", "7th Floor",
            "8th Floor", "9th Floor", "10th Floor", "11th Floor",
            "12th Floor", "13th Floor", "14th Floor", "15th Floor"]

print(
    "Lists of Floors:\n Ground Floor, 1st Floor, 2nd Floor, 3rd Floor\n 4th Floor, 5th floor, 6th Floor, 7th Floor\n"
    " 8th Floor, 9th Floor, 10th Floor, 11th Floor\n 12th Floor, 13th Floor, 14th Floor, 15th Floor")

c_floor = int(input("Enter your current floor: "))

while True:
    t_floor = int(input("Enter the floor you want to reach: "))

    if t_floor < 0 or t_floor > 15:
        print("Invalid floor number. Please enter a floor between 0 and 15.")
        continue

    if t_floor > c_floor:
        for x in range(c_floor, t_floor):
            print("Going Up %s Floor" % x)
            time.sleep(1)
    elif t_floor < c_floor:
        for x in range(c_floor, t_floor, -1):
            print("Going Down %s Floor" % (x - 1))
            time.sleep(1)

    c_floor = t_floor
    print("You are now at the:", elevator[c_floor])

    choice = input("Do you want to continue to another floor? (yes/no): ")
    if choice.lower() != "yes":
        break
