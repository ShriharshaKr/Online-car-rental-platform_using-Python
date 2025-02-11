# Online Car Rental Platform

## 📌 Project Overview
This project is a simple **Online Car Rental Platform** built using **Python** and **Object-Oriented Programming (OOP)** principles. It allows customers to rent cars on an **hourly, daily, or weekly** basis, view available inventory, and receive auto-generated bills.

## 🎯 Features
- 🏎 View available cars for rent.
- ⏳ Rent cars on **hourly, daily, or weekly** basis.
- 📋 Return rented cars and generate a detailed bill.
- 🛠 Inventory management for rental companies.

## 🛠 Technologies Used
- **Programming Language:** Python  
- **Environment:** Jupyter Notebook  
- **Modules Used:**
  - `datetime` (for time tracking)  
  - Custom modules: `CarRental` and `Customer`  

## 🏗 Implementation Details

### **1️⃣ CarRental Module**
Handles car inventory, rental operations, and billing.

**Main Methods:**
- `display_cars()` → Shows available cars.
- `rent_hourly(num_of_cars)` → Hourly rental.
- `rent_daily(num_of_cars)` → Daily rental.
- `rent_weekly(num_of_cars)` → Weekly rental.
- `return_car(rental_time, rental_mode, num_of_cars)` → Calculates bill and updates inventory.

### **2️⃣ Customer Module**
Handles customer interactions.

**Main Methods:**
- `request_car(num_of_cars)` → Requests cars for rent.
- `return_car()` → Returns rented cars.

### **3️⃣ Main Script**
Integrates both modules to provide a user-friendly experience.

## 💰 Billing System
- **Hourly Rate:** $5/hour  
- **Daily Rate:** $20/day  
- **Weekly Rate:** $60/week  
- The system calculates bills based on rental duration and the number of cars rented.

## 🚀 Future Enhancements
- 🔹 Store rental data in a **database** for persistence.  
- 🔹 Implement **user authentication** for security.  
- 🔹 Create a **web-based interface** for better accessibility.  
- 🔹 Add **discounts and loyalty programs**.  

## 📜 Conclusion
This project demonstrates **Python OOP concepts** in a practical scenario. It is designed for ease of use and maintainability while providing a streamlined car rental service.

---

### 🎯 **How to Run the Project**
1. Download or clone the repository.  
2. Open **Jupyter Notebook** and run the scripts.  
3. Follow the prompts in the console to rent and return cars.  

🚀 Happy Coding!
