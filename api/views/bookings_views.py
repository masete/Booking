from flask import Blueprint, jsonify, request
from flask_jwt_extended import (jwt_required, get_jwt_identity, create_access_token)
from api.models.car_staff_model import Car
from api.models.room_staff_model import Room

car = Car()
room = Room()

staff_blueprint = Blueprint("staff", __name__)


@staff_blueprint.route('/api/v1/book_a_car', methods=['POST'], strict_slashes=False)
@jwt_required
def create_a_car_booking():
    data = request.get_json()

    try:
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        trip_destination = data.get('trip_destination')
        pourpose = data.get('pourpose')
        depature_time = data.get('depature_time')
        expected_return_time = data.get('expected_return_time')

    except KeyError:
        return (
            jsonify(
                {
                    "error": "Please provide the correct keys for the data",
                    "status": 422,
                }
            ),
            422,
        )

    request_car = car.insert_new_booking(first_name, last_name, trip_destination, pourpose, depature_time, expected_return_time)

    if request_car:
        return jsonify({'message': "booking with pourpose {} has been added".format(pourpose)}), 201
    return jsonify({'message': "booking not added"}), 400


@staff_blueprint.route('/api/v1/get_all_bookings', methods=['GET'], strict_slashes=False)
@jwt_required
def get_my_bookings():

    all_bookings = car.get_all_car_booking()
    return jsonify({"message": all_bookings})


@staff_blueprint.route('/api/v1/get_single_booking/<int:booking_id>', methods=['GET'], strict_slashes=False)
@jwt_required
def get_single_booking(booking_id):
    single_booking = car.get_booking_by_staff_id(booking_id)
    if not single_booking:
        return jsonify({"message": "parcel does not exist"}), 404
    return jsonify({"single_parcel": single_booking}), 200


@staff_blueprint.route('/api/v1/book_a_room', methods=['POST'], strict_slashes=False)
@jwt_required
def book_a_room():
    data = request.get_json()
    try:
        room_name = data.get('room_name')
        meeting_name = data.get('meeting_name')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        meeting_duraion = data.get('meeting_duration')

    except KeyError:
        return (
            jsonify(
                {
                    "error": "Please provide the correct keys for the data",
                    "status": 422,
                }
            ),
            422,
        )

    room_record = room.insert_room_booking(room_name, meeting_name, start_time, end_time, meeting_duraion)

    if room_record:
        return jsonify({'message': "request to book room has been submitted"}), 201
    return jsonify({'message': "request failed"}), 400


@staff_blueprint.route('/api/v1/get_all_room_bookings', methods=['GET'], strict_slashes=False)
@jwt_required
def get_my_room_bookings():

    all_bookings = room.get_all_room_booking()
    return jsonify({"message": all_bookings})


@staff_blueprint.route('/api/v1/get_single_room_booking/<int:room_booking_id>', methods=['GET'], strict_slashes=False)
@jwt_required
def get_one_room_booking(room_booking_id):
    single_booking = room.get_booking_by_id(room_booking_id)
    if not single_booking:
        return jsonify({"message": "parcel does not exist"}), 404
    return jsonify({"single_room": single_booking}), 200


# admin endpoint
@staff_blueprint.route('/api/v1/approve_car_booking/<int:booking_id>', methods=['PUT'], strict_slashes=False)
@jwt_required
def edit_car_request_status(booking_id):

    user_role = get_jwt_identity()

    if user_role['as_admin'] != True:
        return jsonify({"message": "your not authorised"}), 401

    data = request.get_json()
    status = data.get('status')

    car_status = car.update_car_approval_status(booking_id, status)
    return jsonify({"message": "car booking status has been changed successfully", "status changed": car_status})


# admin endpoint
@staff_blueprint.route('/api/v1/approve_room_booking/<int:room_booking_id>', methods=['PUT'], strict_slashes=False)
@jwt_required
def edit_room_request_status(room_booking_id):

    user_role = get_jwt_identity()

    if user_role['as_admin'] != True:
        return jsonify({"message": "your not authorised"}), 401

    data = request.get_json()
    status = data.get('status')

    room_status = room.update_room_approval_status(room_booking_id, status)
    return jsonify({"message": "room booking status has been changed successfully", "status changed": room_status})


# admin endpoint
@staff_blueprint.route('/api/v1/get_all_approved_car_requests', methods=['GET'], strict_slashes=False)
@jwt_required
def get_all_approved_car_requests():

    approved_cars = car.get_all_approved_cars()
    return jsonify({"message": "List of all approved travels", "data": approved_cars}), 200


# admin endpoint
@staff_blueprint.route('/api/v1/get_all_approved_room_requests', methods=['GET'], strict_slashes=False)
@jwt_required
def get_all_approved_room_requests():
    approved_rooms = room.get_all_approved_room()
    return jsonify({"message": "List of all approved travels", "data": approved_rooms}), 200



