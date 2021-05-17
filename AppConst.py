"""
This module is used to store the input & output file path and input & output messages
"""

import os

input_output_file_path = os.getcwd() + '\\inputoutput\\'
input_csv_file_name = 'employee.csv'
output_file_name = 'extracted_employee.json'

input_file_not_found_msg = 'Input file is not available. Please check.'
name_empty_msg = 'Both First and Last name is empty'
incorrect_date_format_msg = 'Either Date of Birth is not in correct format'
joining_quarter_empty_msg = 'Quarter of Joining is empty'
invalid_quarter_value_msg = 'Quarter value is invalid'
