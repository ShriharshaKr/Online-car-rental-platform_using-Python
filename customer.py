

# Main project file: main_project.ipynb
from Car_Rental import Car_Rental
from Car_Rental import Customer

def main():
    rental_shop = Car_Rental(50)
    customer = Customer()

    while True:
        print("\nWelcome to the Online Car Rental Platform")
        print("1. Display available cars")
        print("2. Rent cars hourly ($5 per hour)")
        print("3. Rent cars daily ($20 per day)")
        print("4. Rent cars weekly ($60 per week)")
        print("5. Return cars")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(rental_shop.display_cars())

        elif choice == 2:
            cars = int(input("How many cars would you like to rent hourly? "))
            rental_time, message = rental_shop.rent_hourly(cars)
            customer.rental_time = rental_time
            customer.rental_mode = 'hourly'
            customer.cars_rented = cars
            print(message)

        elif choice == 3:
            cars = int(input("How many cars would you like to rent daily? "))
            rental_time, message = rental_shop.rent_daily(cars)
            customer.rental_time = rental_time
            customer.rental_mode = 'daily'
            customer.cars_rented = cars
            print(message)

        elif choice == 4:
            cars = int(input("How many cars would you like to rent weekly? "))
            rental_time, message = rental_shop.rent_weekly(cars)
            customer.rental_time = rental_time
            customer.rental_mode = 'weekly'
            customer.cars_rented = cars
            print(message)

        elif choice == 5:
            rental_details = customer.return_car()
            if isinstance(rental_details, tuple):
                rental_time, rental_mode, num_of_cars = rental_details
                print(rental_shop.return_car(rental_time, rental_mode, num_of_cars))
            else:
                print(rental_details)

        elif choice == 6:
            print("Thank you for using the Online Car Rental Platform!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()