from abc import ABC, abstractmethod


class RepairService(ABC):

    def __init__(self, service_id, name, labor_cost, status="Pending"):
        self.service_id = service_id
        self.name = name
        self.__labor_cost = labor_cost
        self.__status = status

    def get_labor_cost(self):
        return self.__labor_cost

    def set_labor_cost(self, cost):

        if cost < 0:
            print("Invalid labor cost.")
        else:
            self.__labor_cost = cost

    def get_status(self):
        return self.__status

    def set_status(self, status):

        valid_status = ["Pending", "In Progress", "Fixed"]

        if status in valid_status:
            self.__status = status
        else:
            print("Invalid status.")

    @abstractmethod
    def calculate_service_cost(self):
        pass

    @abstractmethod
    def display_service_info(self):
        pass


class HardwareRepair(RepairService):

    def __init__(self, service_id, name, labor_cost,
                 part_cost, warranty_period):

        super().__init__(service_id, name, labor_cost)

        self.part_cost = part_cost
        self.warranty_period = warranty_period

    def calculate_service_cost(self):

        subtotal = self.get_labor_cost() + self.part_cost
        tax = subtotal * 0.10

        return subtotal + tax

    def display_service_info(self):

        print(f"[{self.service_id}] {self.name}")
        print(f"Labor Cost: ${self.get_labor_cost():.2f}")
        print(f"Part Cost: ${self.part_cost:.2f}")
        print(f"Warranty: {self.warranty_period} months")
        print(f"Status: {self.get_status()}")
        print("-" * 40)


class SoftwareRepair(RepairService):

    def __init__(self, service_id, name, labor_cost,
                 license_key, os_version):

        super().__init__(service_id, name, labor_cost)

        self.license_key = license_key
        self.os_version = os_version

    def calculate_service_cost(self):

        digital_fee = 5

        return self.get_labor_cost() + digital_fee

    def display_service_info(self):

        print(f"[{self.service_id}] {self.name}")
        print(f"Labor Cost: ${self.get_labor_cost():.2f}")
        print(f"OS Version: {self.os_version}")
        print(f"License Key: {self.license_key}")
        print(f"Status: {self.get_status()}")
        print("-" * 40)


class CustomerInvoice:

    def __init__(self):
        self.repairs = []

    def add_repair(self, repair):

        self.repairs.append(repair)

        print(f"{repair.name} added successfully.")

    def show_invoice(self):

        if not self.repairs:
            print("Invoice is empty.")
            return

        print("\n========== CURRENT INVOICE ==========")

        for repair in self.repairs:

            print(f"{repair.name} --> "
                  f"${repair.get_labor_cost():.2f}")

        print("=====================================")

    def print_final_bill(self):

        if not self.repairs:
            print("No repairs added.")
            return

        print("\n===================================")
        print("       TECH REPAIR SHOP BILL")
        print("===================================")

        total = 0

        for repair in self.repairs:

            cost = repair.calculate_service_cost()

            total += cost

            print(f"{repair.name:<25} ${cost:.2f}")

        print("-----------------------------------")
        print(f"TOTAL BILL:             ${total:.2f}")
        print("===================================")


services = [

    HardwareRepair(
        1,
        "Laptop Screen Replacement",
        50,
        120,
        6
    ),

    HardwareRepair(
        2,
        "Battery Replacement",
        30,
        60,
        3
    ),

    SoftwareRepair(
        3,
        "Windows Installation",
        40,
        "WIN-KEY-2026",
        "Windows 11"
    ),

    SoftwareRepair(
        4,
        "Virus Removal",
        25,
        "SAFE-KEY",
        "Windows 10"
    )
]


def view_services():

    print("\n========== AVAILABLE SERVICES ==========")

    for service in services:
        service.display_service_info()


def find_service(user_input):

    for service in services:

        if str(service.service_id) == user_input:
            return service

        if service.name.lower() == user_input.lower():
            return service

    return None


def main():

    invoice = CustomerInvoice()

    while True:

        print("\n========= TECH REPAIR SHOP =========")
        print("1. View Services")
        print("2. Add Service to Invoice")
        print("3. View Current Invoice")
        print("4. Print Final Bill")
        print("5. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            view_services()

        elif choice == "2":

            user_input = input(
                "Enter Service ID or Service Name: "
            )

            service = find_service(user_input)

            if service:
                invoice.add_repair(service)

            else:
                print("Service not found.")

        elif choice == "3":

            invoice.show_invoice()

        elif choice == "4":

            invoice.print_final_bill()

        elif choice == "5":

            print("Thank you for using the system.")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()