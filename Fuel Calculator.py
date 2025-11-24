
def calculate_fuel(distance, mileage):
    fuel = distance / mileage
    return fuel


def calculate_cost(fuel, price):
    cost = fuel * price
    return cost


def show_menu():
    print("  FUEL CONSUMPTION CALCULATOR")
    print("")
    print("1. Add Vehicle Mileage")
    print("2. View Mileage List")
    print("3. Calculate Trip Cost")
    print("4. Save Report to File")
    print("5. Exit")
  


print("\nWelcome to the Fuel Consumption and Trip Cost Calculator")


distance = float(input("Enter distance to travel (in km): "))
price = float(input("Enter current fuel price per liter: "))

mileages = []       # to store mileages of vehicles
fuel_list = []      # stores fuel required for each vehicle
cost_list = []      # stores cost of the trip for each vehicle
report_data = ""    # string to save final report

while True:
    show_menu()
    choice = int(input("Enter your choice (1-5): "))

    
    if choice == 1:
        count = int(input("How many vehicles you want to add? "))
        for i in range(count):
            m = float(input(f"Enter mileage of vehicle {len(mileages)+1} (km/l): "))
            mileages.append(m)
        print("Mileage added successfully!")
    elif choice == 2:
        if len(mileages) == 0:
            print("No vehicles added yet!")
        else:
            print("\nList of Vehicle Mileages:")
            for i in range(len(mileages)):
                print(f"Vehicle {i+1} → {mileages[i]} km/l")

  
    elif choice == 3:
        if len(mileages) == 0:
            print("Please add mileage first!")
            continue

        fuel_list.clear()
        cost_list.clear()

        print("Trip Cost Summary")
        print("Vehicle\tMileage\tFuel Needed (L)\tTrip Cost (INR)")

        report_data = "Vehicle\tMileage\tFuel Needed\tTrip Cost\n"

        for i in range(len(mileages)):
            fuel = calculate_fuel(distance, mileages[i])
            cost = calculate_cost(fuel, price)

            fuel_list.append(fuel)
            cost_list.append(cost)

            print(f"{i+1}\t{mileages[i]}\t{fuel:.2f}\t\t{cost:.2f}")

            report_data += f"{i+1}\t{mileages[i]}\t{fuel:.2f}\t{cost:.2f}\n"

      
        min_cost = min(cost_list)
        best_vehicle = cost_list.index(min_cost) + 1

        
        print(f"Cheapest option: Vehicle {best_vehicle} with cost {min_cost:.2f} INR")
        print("")

        report_data += f"\nCheapest Vehicle: {best_vehicle}   Cost: {min_cost:.2f} INR\n"


    elif choice == 4:
        if report_data == "":
            print("No report generated yet! Calculate cost first.")
        else:
            with open("trip_report.txt", "w") as f:
                f.write("FUEL CONSUMPTION REPORT\n")
                f.write("")
                f.write(report_data)
            print("Report saved successfully as 'trip_report.txt'!")

  
    elif choice == 5:
        print("Thank you for using the Fuel Calculator. Goodbye!")
        break

   
    else:
        print("Invalid choice! Please choose again.")
