"""
This module is used to process the data as per business requirement
"""


def create_quarterly_dict(employee_obj, quarter_dict):
    quarter_dict[employee_obj.joining_quarter].append([employee_obj.get_full_name(), employee_obj.parse_dob()])
    return quarter_dict


def sort_quarterly_dict(quarter_dict):
    for value in quarter_dict.values():
        value.sort(key=lambda x: x[1])


def remove_dob(quarter_dict):
    temp_dict = dict()
    for key, value in quarter_dict.items():
        temp_list = list()

        for name_list in value:
            temp_list.append(name_list[0])

        temp_dict[key] = temp_list

    return temp_dict


