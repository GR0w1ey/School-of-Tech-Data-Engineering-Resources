import csv
from datetime import datetime
from sql_utils import setup_db_connection, insert_students

def read_csv_to_list(filename):
    print(f'read_csv_to_list: opening {filename}...')
    with open(filename, newline='') as file:
        return list(csv.DictReader(file, delimiter=','))

 
def convert_all_dates(list_of_dicts, date_cols,
                      current_format='%d/%m/%Y',
                      expected_format='%Y-%m-%d'):
    print(f'convert_all_dates...')
    for dict in list_of_dicts:
        for col in date_cols:
            try:
                str_to_date = datetime.strptime(dict[col], current_format)
                date_to_str = datetime.strftime(str_to_date, expected_format)
                dict[col] = date_to_str
            except ValueError:
                dict[col] = None
    return list_of_dicts


def check_integer_columns(list_of_dicts, int_cols):
    # print(f'check_integer_columns...')
    
    for dict_element in list_of_dicts:
        for col in int_cols:
            try:
                dict_element[col] = int(dict_element[col])
            except ValueError as VE:
                dict_element[col] = None

    return list_of_dicts

def check_values_in_valid_list(list_of_dicts, valid_items, col_name):
    print(f'check_values_in_valid_list...')
    for dict_element in list_of_dicts:
        if dict_element[col_name] in valid_items:
            continue
        else:
            dict_element[col_name] = None
    
    return list_of_dicts


def drop_duplicate_ids(list_of_dicts):
    print(f'drop_duplicate_ids...')
    
    existing_ids = []
    new_dictionaries_list = []

    for dict_element in list_of_dicts:
        if dict_element['id'] in existing_ids:
            continue
        else:
            existing_ids.append(dict_element['id'])
            new_dictionaries_list.append(dict_element)

    return new_dictionaries_list


def drop_rows_with_null(list_of_dicts):
    print(f'drop_rows_with_null...')
    return [dict_element for dict_element in list_of_dicts if all(dict_element.values())]

if __name__ == '__main__':

    data_list = read_csv_to_list('messy-data.csv')

    # Sample data:
    #
    # id, name,       age, branch,           teacher, start_date, tel
    # 1,  John Smith, 19,  Computer Sciense, Mrs. X,  13/01/2020, 012345
    #
    # my_list = [
    #     {
    #         'id': 1,
    #         'name': 'John Smith',
    #         'age': None,
    #         'branch': 'Computer Sciense',
    #         'teacher': 'Mrs. X',
    #         'start_date': '13/01/2020',
    #         'tel': 012345
    #     },
    #     {...},
    #     {...},
    #     {...}
    # ]

    data_list = convert_all_dates(data_list, ['start_date'])
    data_list = check_integer_columns(data_list, ['id', 'age'])

    teacher_list = ['Mrs. X', 'Ms. Smith', 'Mr. G']
    data_list = check_values_in_valid_list(data_list, teacher_list, 'teacher')

    data_list = drop_duplicate_ids(data_list)
    data_list = drop_rows_with_null(data_list)

    connection, cursor = setup_db_connection()
    insert_students(connection, cursor, data_list)

    cursor.close()
    connection.close()
