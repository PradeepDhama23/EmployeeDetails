"""
This module is used to check the data consistency, whether input file exists and other validations
"""
from os import path
from AppConst import input_file_not_found_msg, name_empty_msg, incorrect_date_format_msg, \
    joining_quarter_empty_msg, invalid_quarter_value_msg
import sys
import re


def check_file_exists(file_path_name):
    if not path.exists(file_path_name):
        print(input_file_not_found_msg)
        sys.exit()

def validate_csv(row):
    error_msg = list()
    error_flag = False

    # When both first name and last name is empty
    if not (row['First Name'] and row['Last Name']):
        error_flag = True
        error_msg.append(name_empty_msg)

    # Check whether the date can be parsed
    temp_date = re.split('/|-', row['Date of Birth'])
    if len(temp_date) != 3:
        error_flag = True
        error_msg.append(incorrect_date_format_msg)

    # When Quarter of Joining is empty
    if not row['Quarter of Joining']:
        error_flag = True
        error_msg.append(joining_quarter_empty_msg)

    # When Quarter of Joining has invalid value
    if row['Quarter of Joining'] not in ['Q1', 'Q2', 'Q3', 'Q4']:
        error_flag = True
        error_msg.append(invalid_quarter_value_msg)

    return error_flag, error_msg