from typing import List
import json
from numbers import Number

GRAND_TOTAL = 0

def parse_arr(data):
    for val in data:
        check_instance_and_parse(val)

def parse_objects(data):
    for k, val in data.items():
        check_instance_and_parse(val)
    

def parse_numbers(val):
    global GRAND_TOTAL
    GRAND_TOTAL += val


def check_instance_and_parse(data):
    if isinstance(data, dict):
        parse_objects(data)
    if isinstance(data, list):
        parse_arr(data)
    if isinstance(data, Number):
        parse_numbers(data)
    # if isinstance(data, str):
    #     return "string"

def main():
    with open('input.txt', 'r') as file:
        data = json.load(file)
    # print(data.get("e"))

    check_instance_and_parse(data)

    print(f'GRAND_TOTAL is {GRAND_TOTAL}')

if __name__ == "__main__":
    main()