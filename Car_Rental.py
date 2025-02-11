import datetime

class Car_Rental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_cars(self):
        return f"We have {self.stock} car(s) available to rent."

    def rent_hourly(self, num_of_cars):
        if num_of_cars <= 0 or num_of_cars > self.stock:
            return "Invalid request."
        else:
            self.stock -= num_of_cars
            now = datetime.datetime.now()
            return now, f"You have rented {num_of_cars} car(s) on an hourly basis."

    def rent_daily(self, num_of_cars):
        if num_of_cars <= 0 or num_of_cars > self.stock:
            return "Invalid request."
        else:
            self.stock -= num_of_cars
            now = datetime.datetime.now()
            return now, f"You have rented {num_of_cars} car(s) on a daily basis."

    def rent_weekly(self, num_of_cars):
        if num_of_cars <= 0 or num_of_cars > self.stock:
            return "Invalid request."
        else:
            self.stock -= num_of_cars
            now = datetime.datetime.now()
            return now, f"You have rented {num_of_cars} car(s) on a weekly basis."

    def return_car(self, rental_time, rental_mode, num_of_cars):
        now = datetime.datetime.now()
        rental_period = now - rental_time

        if rental_mode == 'hourly':
            bill = rental_period.seconds / 3600 * 5 * num_of_cars
        elif rental_mode == 'daily':
            bill = rental_period.days * 20 * num_of_cars
        elif rental_mode == 'weekly':
            bill = (rental_period.days / 7) * 60 * num_of_cars
        else:
            return "Invalid rental mode."

        self.stock += num_of_cars
        return f"Your bill is ${bill:.2f}. Thank you for returning the car(s)!"

class Customer:
    def __init__(self):
        self.cars_rented = 0
        self.rental_time = None
        self.rental_mode = None

    def request_car(self, num_of_cars):
        if num_of_cars <= 0:
            return "Invalid input."
        else:
            self.cars_rented = num_of_cars
            return f"You have requested {num_of_cars} car(s)."

    def return_car(self):
        if self.rental_time and self.rental_mode and self.cars_rented:
            return self.rental_time, self.rental_mode, self.cars_rented
        else:
            return "You did not rent any car(s)."