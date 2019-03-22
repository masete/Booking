from api.models.database import DatabaseConnection


class Room:
    cursor = DatabaseConnection().cursor

    def __init__(self, room_booking_id=None, room_name=None, meeting_name=None, start_time=None, end_time=None,
                 meeting_duration=None, status=None):
        self.room_booking_id = room_booking_id
        self.room_name = room_name
        self.meeting_name = meeting_name
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_duration = meeting_duration
        self.status = status
      
    def insert_room_booking(self, room_name, meeting_name, start_time, end_time, meeting_duration, status):
        insert_booking = "INSERT INTO room_booking(room_name, meeting_name, start_time, end_time, meeting_duration, status)" \
                         " VALUES('{}','{}','{}','{}','{}','{}')".format(room_name, meeting_name, start_time, end_time,
                                                                    meeting_duration, status)
        self.cursor.execute(insert_booking)
        return True

    def get_all_room_booking(self):
        get_all_booking = "SELECT * FROM room_booking"
        self.cursor.execute(get_all_booking)
        results = self.cursor.fetchall()
        return results

    def get_booking_by_id(self, room_booking_id):
        get_single_booking = "SELECT * FROM room_booking WHERE room_booking_id = {}".format(room_booking_id)
        self.cursor.execute(get_single_booking)
        result = self.cursor.fetchone()
        return result
