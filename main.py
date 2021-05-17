"""
This is main file of the application, where reading CSV and then getting the desired output
"""
from AppConst import *
from util import validator, write
from business import serialize, business_logic
import csv
from collections import defaultdict


if __name__ == '__main__':

    quarter_dict = defaultdict(list)

    # Check whether the input file exists
    csv_file_path = input_output_file_path + input_csv_file_name
    validator.check_file_exists(csv_file_path)

    # Read CSV file using csv package and load data in dictionary
    csv_file = open(csv_file_path, mode='r', encoding='utf-8')
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:

        # Check data in csv file
        error_flag, error_msg = validator.validate_csv(row)
        if error_flag:
            print('The emp-id: {} is not processed due to following error: '.format(row['Emp ID']))
            for error in error_msg:
                print(error)
            continue

        # Creating Employee object
        employee_obj = serialize.create_employee_object(row)

        # Creating default dictionary
        quarter_dict = business_logic.create_quarterly_dict(employee_obj, quarter_dict)

    # Close csv file
    csv_file.close()

    # Sort the dictionary by DOB
    business_logic.sort_quarterly_dict(quarter_dict)

    # Remove DOB element from dictionary
    final_dict = business_logic.remove_dob(quarter_dict)

    #print(quarter_dict)
    #print(final_dict)


    write.write_display(final_dict)