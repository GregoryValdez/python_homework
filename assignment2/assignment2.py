import csv # Task 2
import traceback

def read_employees():
    data = {} # empty dictionary
    rows = [] # empty list
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    data['fields'] = row # store first row in the key 'fields'
                    first = False
                else:
                    rows.append(row) # store all others to rows list
        data['rows'] = rows # add list of rows to dictionary in the key 'rows'
        return data
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message: 
            print(f"Exception message: {message}")
        print(f'Stack trace: {stack_trace}')
employees = read_employees()
print(employees)

def column_index(column_name): # Task 3
    # Needs a parameter 
    try:
        return employees['fields'].index(column_name)
    except ValueError:
        return f'Column name {column_name} not found.'
employee_id_column = column_index('employee_id')
print(employee_id_column)

def first_name(row_num): # Task 4
    try:
        index = column_index('first_name')
        return employees['rows'][row_num][index] # Input is row number, output is first name in that row
    except IndexError:
        return f'Row number {row_num} is out of range.'

def employee_find(employee_id): # Task 5
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id # for row of rows, check if employee_id_column matches the input employee_id 
        matches = list(filter(employee_match, employees['rows'])) # Output is list[] of the row that matches employee_id
        return matches 
    except Exception as e:
        return f'Employee id: {e} not found.'

def employee_find_2(employee_id): # Task 6
    try:
        matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees['rows'])) # same as above but with lambda function
        return matches 
    except Exception as e:
        return f'Employee id: {e} not found.'

def sort_by_last_name(): # Task 7
    try:
        employees['rows'].sort(key=lambda row: row[column_index('last_name')]) # lambda is passed the row. Then sorts the rows by the last name column
        return employees['rows'] 
    except Exception as e:
        return f'Error sorting by last name: {e}'
print(sort_by_last_name())

def employee_dict(employee_row): # Task 8
    try:
        dict = {}
        for i in range(len(employees['fields'])): # for each field, add the field as a key and the corresponding value from employee_row as the value
            dict[employees['fields'][i]] = employee_row[i]
        del dict['employee_id'] # delete column
        return dict
    except Exception as e:
        return f'Error creating employee dictionary: {e}'

def all_employees_dict(): # Task 9
    try:
        dict = {}
        for row in employees['rows']: # for each row, add the employee_id as the key and the employee_dict of that row as the value
            dict[row[employee_id_column]] = employee_dict(row) # task 3 and task 8 functions
        return dict
    except Exception as e:
        return f'Error creating all employees dictionary: {e}' 
print(all_employees_dict())

import os 
def get_this_value(): # Task 10
    try:
        return os.getenv('THISVALUE') 
    except Exception as e:
        return f'Error getting environment variable: {e}'
# export THISVALUE=ABC (Enter in the terminal to pass test)

import custom_module
def set_that_secret(update_secret): # Task 11
    try:
        return custom_module.set_secret(update_secret)
    except Exception as e:
        return f'Error setting secret: {e}'
print(set_that_secret('superdunk'))
print(custom_module.secret)

def read_minutes(): # Task 12
    try: 
        def upload_minutes(path):
            with open(path, 'r') as file:
                reader = csv.reader(file)
                fields = next(reader) # Reads the first line of csv, splits it into column names, & stores that list in variable fields.
                rows = [tuple(row) for row in reader] # Gets all remaining rows in the rows list[], each converted to tuples
                return {'fields': fields, 'rows': rows}
        minutes1 = upload_minutes('../csv/minutes1.csv')
        minutes2 = upload_minutes('../csv/minutes2.csv')
        return minutes1, minutes2 
    except Exception as e:
        return f'Error reading minutes: {e}'
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

def create_minutes_set(): # Task 13
    try:
        # Convert the rows lists into sets{}. Sets only support hashable elements which tuples() are, but not lists[]
        set1 = set(minutes1['rows'])
        set2 = set(minutes2['rows'])
        combine = set1.union(set2) # Returns a set containing all unique elements from both sets
        return combine 
    except Exception as e:
        return f'Error setting rows: {e}'
minutes_set = create_minutes_set()
print(minutes_set)

from datetime import datetime
def create_minutes_list(): # Task 14
    try:
        minutes_list_convert = list(minutes_set)
        convert = map(lambda x: (x[0], datetime.strptime(x[1], '%B %d, %Y')), minutes_list_convert) # Map each tuple to (name, datetime_object)
        return list(convert) # Convert map object to list
    except Exception as e:
        return f'Error converting: {e}'
minutes_list = create_minutes_list()
print(minutes_list)

def write_sorted_list(): # Task 15
    try:
        sorted_list = sorted(minutes_list, key=lambda x: x[1]) # Sort minutes_list by datetime (x[1])
        convert = list(map(lambda x: (x[0], x[1].strftime('%B %d, %Y')), sorted_list)) # Convert datetime objects back to strings
        with open('./minutes.csv', 'w', newline='') as file:
            # Write to ./minutes.csv
            writer = csv.writer(file) 
            writer.writerow(minutes1['fields']) # Write header row from minutes1
            for row in convert:
                # Write each row of converted data
                writer.writerow(row)
        return convert 
    except Exception as e:
        return f'Error sorting list: {e}'
sorted_written_list = write_sorted_list()
print(sorted_written_list)