from flask_restful import reqparse

from app.algohub.algorithms.numbers.digits import (
    get_digit,
    sum_digits,
    sum_range,
    validate_luhn,
    move_zeroes
)
from flask import Response, request, jsonify

from flask import Blueprint
import logging

logging.basicConfig(level=logging.INFO)

digits_blueprint = Blueprint('digits', __name__, url_prefix='/digits')

# todo wszystko zrobione z digits.

# blad prechwyci route z maina, a blad bedzie rzucony w funkjci get_digit
@digits_blueprint.route('/get_digit/<int:number>', methods=['GET'])
def get_digit_(number: int):
    position = request.args.get('position', default=0, type=int)
    digit = get_digit(number, position)
    return jsonify({'digit': digit}), 201


@digits_blueprint.route('/sum_digits/<int:number>', methods=['GET'])
def sum_digits_(number: int):
    digits_sum = sum_digits(number)
    return jsonify({'digits_sum': digits_sum}), 201


@digits_blueprint.route('/sum_range', methods=['GET'])
def sum_range_():
    parser = reqparse.RequestParser()
    parser.add_argument('r_start', type=int)
    parser.add_argument('r_end', type=int)
    json_body = parser.parse_args()
    a, b = json_body['r_start'], json_body['r_end']
    return jsonify({'sum_range': sum_range(a, b)}), 201


@digits_blueprint.route('/move_zeroes', methods=['GET'])
def move_zeroes_():
    parser = reqparse.RequestParser()
    parser.add_argument('numbers', type=list, location='json', help='List of numbers')
    request_data = parser.parse_args()
    numbers = request_data['numbers']
    if 0 not in numbers:
        return jsonify({'No zeroes to move': numbers}), 201
    move_zeroes(numbers)
    return jsonify({'Zeroes moved successfully to the end': numbers}), 201


