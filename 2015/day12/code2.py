from typing import List
import json
from numbers import Number

def parse_arr(data):
    curr_object_total = 0
    def increment_curr_total(val):
        nonlocal curr_object_total
        curr_object_total += val

    for val in data:
        instance_type = check_instance_and_parse(val)
        if instance_type == "dict":
            increment_curr_total(parse_objects(val))
        elif instance_type == "list":
            increment_curr_total(parse_arr(val))
        elif instance_type == "number":
            increment_curr_total(val)
    return curr_object_total

def parse_objects(data):
    curr_object_total = 0
    def increment_curr_total(val):
        nonlocal curr_object_total
        curr_object_total += val

    for k, val in data.items():
        instance_type = check_instance_and_parse(val)
        if instance_type == "dict":
            increment_curr_total(parse_objects(val))
        elif instance_type == "list":
            increment_curr_total(parse_arr(val))
        elif instance_type == "string":
            if not is_string_red(val) == "danger":
                return 0
        elif instance_type == "number":
            increment_curr_total(val)
    return curr_object_total
        
def is_string_red(data):
    if data == "red":
        return False
    return True

def check_instance_and_parse(data):
    if isinstance(data, dict):
        return "dict"
    if isinstance(data, list):
        return "list"
    if isinstance(data, Number):
        return "number"
    if isinstance(data, str):
        return "string"

def main():
    with open('input.txt', 'r') as file:
        data = json.load(file)
    # print(data.get("e"))
    GRAND_TOTAL = 0
    instance_type = check_instance_and_parse(data)
    if instance_type == "dict":
        GRAND_TOTAL = parse_objects(data)
    elif instance_type == "list":
        GRAND_TOTAL = parse_arr(data)
    elif instance_type == "number":
        GRAND_TOTAL = data

    print(f'GRAND_TOTAL is {GRAND_TOTAL}')

if __name__ == "__main__":
    main()