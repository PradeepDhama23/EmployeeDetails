"""
This module is used to serialize employee csv data using employee class
"""
from model.Employee import Employee

def create_employee_object(row):
    employee_obj = Employee(row['Emp ID'],
                            row['First Name'],
                            row['Last Name'],
                            row['Gender'],
                            row['Father\'s Name'],
                            row['Mother\'s Name'],
                            row['Mother\'s Maiden Name'],
                            row['Date of Birth'],
                            row['Date of Joining'],
                            row['Quarter of Joining'],
                            row['Place Name'],
                            row['County'],
                            row['City'],
                            row['State'],
                            row['Zip'],
                            row['User Name'])
    return employee_obj
