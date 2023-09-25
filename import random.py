class MechanicShop:
    def __init__(self):
        self.vehicles = {}
        self.parts = {
            "engine": 1000,
            "battery": 100,
            "tire": 50,
            "brake": 20,
            "oil": 10
        }
        self.receipts = {}

    def add_vehicle(self):
        license_plate = input("Enter the license plate number of your vehicle: ")
        make = input("Enter the make of your vehicle: ")
        model = input("Enter the model of your vehicle: ")
        year = input("Enter the year of your vehicle: ")

        vehicle = {
            "license_plate": license_plate,
            "make": make,
            "model": model,
            "year": year
        }

        self.vehicles[license_plate] = vehicle

    def modify_vehicle(self):
        license_plate = input("Enter the license plate number of the vehicle you want to modify: ")

        if license_plate not in self.vehicles:
            raise ValueError("Vehicle does not exist.")

        vehicle = self.vehicles[license_plate]

        make = input("Enter the new make of your vehicle: ")
        model = input("Enter the new model of your vehicle: ")
        year = input("Enter the new year of your vehicle: ")

        vehicle["make"] = make
        vehicle["model"] = model
        vehicle["year"] = year

    def describe_problem(self):
        problem = input("Please describe your problem in detail: ")
        return problem

    def diagnose_problem(self, problem):
        return problem

    def schedule_appointment(self, problem):
        print("Thank you for your description. We will be in contact with you shortly to schedule an appointment.")

    def order_parts(self, problem):
        problems_and_parts = {
            "engine failure": ["engine"],
            "battery dead": ["battery"],
            "flat tire": ["tire"],
            "brake malfunction": ["brake"],
            "oil leak": ["oil"]
        }

        if problem in problems_and_parts:
            parts_needed = problems_and_parts[problem]
            total_cost = 0

            for part in parts_needed:
                total_cost += self.parts[part]

            print(f"The parts needed for your repair are {parts_needed}. The total cost is ${total_cost}.")
            print("We have placed an order for these parts, and they will arrive soon.")
        else:
            print("We are sorry, but we do not have a solution for your problem at this time.")

    def generate_receipt(self, license_plate, problem):
        if license_plate not in self.vehicles or problem not in self.parts:
            raise ValueError("Invalid license plate or problem.")
        vehicle = self.vehicles[license_plate]
        receipt = self.receipts[problem]

        vehicle = self.vehicles[license_plate]
        part_cost = self.parts[problem]
        service_fee = part_cost * 0.1
        total_amount = part_cost + service_fee
       

        receipt = f"Receipt for Vehicle:\n"
        receipt += f"License Plate: {vehicle['license_plate']}\n"
        receipt += f"Make: {vehicle['make']}\n"
        receipt += f"Model: {vehicle['model']}\n"
        receipt += f"Year: {vehicle['year']}\n"
        receipt += f"Problem: {problem}\n"
        receipt += f"Part Cost: ${part_cost}\n"
        receipt += f"Service Fee: ${service_fee}\n"
        receipt += f"Total Amount: ${total_amount}\n"

        self.receipts[license_plate] = receipt

    def print_receipt(self, license_plate):
        if license_plate not in self.receipts:
            raise ValueError("Invalid license plate.")

        receipt = self.receipts[license_plate]
        print(receipt)

    def simulate(self):
        while True:
            print("Welcome to the mechanic shop!")

            print("What would you like to do today?")
            print("1. Add a vehicle")
            print("2. Modify a vehicle")
            print("3. Describe a problem")
            print("4. Order parts")
            print("5. Generate receipt")
            print("6. Print receipt")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                self.add_vehicle()
            elif choice == "2":
                self.modify_vehicle()
            elif choice == "3":
                problem = self.describe_problem()
                diagnosed_problem = self.diagnose_problem(problem)
                self.schedule_appointment(diagnosed_problem)
            elif choice == "4":
                problem = input("Enter the problem you want to order parts for: ")
                self.order_parts(problem)
            elif choice == "5":
                license_plate = input("Enter the license plate number of the vehicle you want to generate a receipt for: ")
                problem = input("Enter the problem that was fixed for your vehicle: ")
                self.generate_receipt(license_plate, problem)
            elif choice == "6":
                license_plate = input("Enter the license plate number of the vehicle you want to print a receipt for: ")
                self.print_receipt(license_plate)
            elif choice == "7":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    mechanic_shop = MechanicShop()
    mechanic_shop.simulate()



  
