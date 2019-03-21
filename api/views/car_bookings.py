"""order.py holding my parcel order views"""
from flask import Blueprint, jsonify, request
from api.models.staff_model import Staff

staff = Staff()

staff_blueprint = Blueprint("parcel", __name__)


@staff_blueprint.route('/api/v1/book_a_car', methods=['POST'], strict_slashes=False)
def create_a_car_booking():
    data = request.get_json()

    try:
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        trip_destination = data.get('trip_destination')
        time = data.get('time')
        pourpose = data.get('pourpose')
    except:
        return jsonify({"message": "bad request"}), 400

    request_car = staff.insert_new_booking(first_name, last_name, trip_destination, time, pourpose)

    if request_car:
        return jsonify({'message': "booking with pourpose {} has been added".format(pourpose)}), 201
    return jsonify({'message': "booking not added"}), 400


@staff_blueprint.route('/api/v1/get_all_bookings', methods=['GET'], strict_slashes=False)
def get_my_bookings():

    all_bookings = staff.get_all_car_booking()
    return jsonify({"message": all_bookings})


@staff_blueprint.route('/api/v1/get_single_booking/<int:booking_id>', methods=['GET'], strict_slashes=False)
def get_single_booking(booking_id):
    single_booking = staff.get_booking_by_staff_id(booking_id)
    if not single_booking:
        return jsonify({"message": "parcel does not exist"}), 404
    return jsonify({"single_parcel": single_booking}), 200






