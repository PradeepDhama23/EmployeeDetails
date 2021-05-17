import re
import datetime

class Employee():

    def __init__(self, emp_id, first_name, last_name, gender, father_name, mother_name, mother_maiden_name,
                dob, doj, joining_quarter, place_name, country, city, state, zip_code, user_name):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.father_name = father_name
        self.mother_name = mother_name
        self.mother_maiden_name = mother_maiden_name
        self.dob = dob
        self.doj = doj
        self.joining_quarter = joining_quarter
        self.place_name = place_name
        self.country = country
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.user_name = user_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def parse_dob(self):
        temp_dob = list(map(int, re.split('/|-', self.dob)))
        dob_datetime = datetime.datetime(temp_dob[2], temp_dob[0], temp_dob[1])
        return dob_datetime
