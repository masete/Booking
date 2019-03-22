from flask import Blueprint, jsonify, request
from api.models.car_staff_model import Car
from api.models.room_staff_model import Room

car = Car()
room = Room()

staff_blueprint = Blueprint("staff", __name__)


@staff_blueprint.route('/api/v1/book_a_car', methods=['POST'], strict_slashes=False)
def create_a_car_booking():
    data = request.get_json()

    try:
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        trip_destination = data.get('trip_destination')
        pourpose = data.get('pourpose')
        depature_time = data.get('depature_time')
        expected_return_time = data.get('expected_return_time')
        status = data.get('status')
    except:
        return jsonify({"message": "bad request"}), 400

    request_car = car.insert_new_booking(first_name, last_name, trip_destination, pourpose, depature_time, expected_return_time, status)

    if request_car:
        return jsonify({'message': "booking with pourpose {} has been added".format(pourpose)}), 201
    return jsonify({'message': "booking not added"}), 400


@staff_blueprint.route('/api/v1/get_all_bookings', methods=['GET'], strict_slashes=False)
def get_my_bookings():

    all_bookings = car.get_all_car_booking()
    return jsonify({"message": all_bookings})


@staff_blueprint.route('/api/v1/get_single_booking/<int:booking_id>', methods=['GET'], strict_slashes=False)
def get_single_booking(booking_id):
    single_booking = car.get_booking_by_staff_id(booking_id)
    if not single_booking:
        return jsonify({"message": "parcel does not exist"}), 404
    return jsonify({"single_parcel": single_booking}), 200


@staff_blueprint.route('/api/v1/book_a_room', methods=['POST'], strict_slashes=False)
def book_a_room():
    data = request.get_json()

    room_name = data.get('room_name')
    meeting_name = data.get('meeting_name')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    meeting_duraion = data.get('meeting_duration')
    status = data.get('status')

    room_record = room.insert_room_booking(room_name, meeting_name, start_time, end_time, meeting_duraion, status)

    if room_record:
        return jsonify({'message': "request to book room has been submitted"}), 201
    return jsonify({'message': "request failed"}), 400


@staff_blueprint.route('/api/v1/get_all_room_bookings', methods=['GET'], strict_slashes=False)
def get_my_room_bookings():

    all_bookings = room.get_all_room_booking()
    return jsonify({"message": all_bookings})


@staff_blueprint.route('/api/v1/get_single_room_booking/<int:room_booking_id>', methods=['GET'], strict_slashes=False)
def get_one_room_booking(room_booking_id):
    single_booking = room.get_booking_by_id(room_booking_id)
    if not single_booking:
        return jsonify({"message": "parcel does not exist"}), 404
    return jsonify({"single_room": single_booking}), 200







