from api.models.database import DatabaseConnection


class Car:
    cursor = DatabaseConnection().cursor

    def __init__(self, booking_id=None, first_name=None, last_name=None, trip_destination=None, pourpose=None, depature_time=None, expected_return_time=None,status=None):
        self.booking_id = booking_id
        self.first_name = first_name
        self.last_name = last_name
        self.trip_destination = trip_destination
        self.pourpose = pourpose
        self.depature_time = depature_time
        self.expected_return_time = expected_return_time
        self.status = status

    def insert_new_booking(self, first_name, last_name, trip_destination, depature_time, expected_return_time, pourpose):
        insert_booking = "INSERT INTO car_booking(first_name,last_name,trip_destination, depature_time, expected_return_time,pourpose)" \
                         " VALUES('{}','{}','{}','{}','{}','{}')".format(first_name, last_name, trip_destination,
                                                                               pourpose, depature_time, expected_return_time)
        self.cursor.execute(insert_booking)
        return True

    def get_all_car_booking(self):
        get_all_booking = "SELECT * FROM car_booking"
        self.cursor.execute(get_all_booking)
        results = self.cursor.fetchall()
        return results

    def get_booking_by_staff_id(self, booking_id):
        get_single_booking = "SELECT * FROM car_booking WHERE booking_id = {}".format(booking_id)
        self.cursor.execute(get_single_booking)
        result = self.cursor.fetchone()
        return result

    def update_car_approval_status(self, booking_id, status):
        update_car_status = "UPDATE car_booking SET status = '{}' WHERE booking_id = '{}'".format(status, booking_id)
        self.cursor.execute(update_car_status)
        query = "SELECT * FROM car_booking WHERE booking_id = '{}'".format(booking_id)
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_all_approved_cars(self):
        approved_cars = "SELECT * FROM car_booking WHERE status != False"
        self.cursor.execute(approved_cars)
        result = self.cursor.fetchall()
        return result





