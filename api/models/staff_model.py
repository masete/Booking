from api.models.database import DatabaseConnection


class Staff:
    cursor = DatabaseConnection().cursor

    def __init__(self, booking_id=None, first_name=None, last_name=None, trip_destination=None, time=None, pourpose=None):
        self.booking_id = booking_id
        self.first_name = first_name
        self.last_name = last_name
        self.trip_destination = trip_destination
        self.time = time
        self.pourpose = pourpose

    def insert_new_booking(self, first_name, last_name, trip_destination, time, pourpose):
        insert_booking = "INSERT INTO car_booking(first_name,last_name,trip_destination,time, pourpose)" \
                         " VALUES('{}','{}','{}','{}','{}')".format(first_name, last_name, trip_destination,
                                                                    time, pourpose)
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

