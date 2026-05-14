# Interactive Tech Repair Shop System 🛠️

## Project Overview
This project is a terminal-based management system for a computer and phone repair shop. It was developed to demonstrate advanced Python OOP concepts as part of the course practical task.

## Features
* **View Services:** Displays available hardware and software repair options.
* **Customer Invoice:** Allows adding services by ID or name to a dynamic bill.
* **Smart Billing:** Automatically calculates totals with specific logic (10% tax for hardware, $5 fee for software).
* **Graceful Exit:** The system closes properly upon user request.

## Technical Implementation (OOP Requirements)
1. **Blueprint (Abstraction):** Created a general template for repair services that cannot be instantiated directly.
2. **Specialization (Inheritance):** Developed specific classes for Hardware (with parts cost/warranty) and Software (with license keys).
3. **Data Protection (Encapsulation):** Protected sensitive attributes like labor cost and status from direct external modification using validation rules.
4. **Smart Behavior (Polymorphism):** All services use `calculate_service_cost()`, but each reacts uniquely based on its type.

## How to Run
1. Make sure Python is installed.
2. Open your terminal or command prompt.
3. Navigate to the project folder and run:
   ```bash
   python Repair_Service.py
