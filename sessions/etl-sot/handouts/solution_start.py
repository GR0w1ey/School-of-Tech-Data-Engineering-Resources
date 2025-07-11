############################################################
#
# ETL example start
#
############################################################

import psycopg2
import os
from dotenv import load_dotenv
import csv
from datetime import datetime


# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

try:

    ### Task 1.1 - EXTRACT

    # 1. Read the sales_data.csv
    # TODO - put code here to load the file
    sales_data = []
    with open("sales_data.csv", 'r', newline='') as sales_data:
        csv_reader = csv.DictReader(sales_data, fieldnames = ['customer_id','purchase_date','purchase_amount','product_id'], delimiter=',')
        next(csv_reader)
        sales_data = [row for row in csv_reader]
        
    ### Task 1.2 - TRANSFORM

    # TODO - put code here for the steps below
    # 2. Clean that data (minimum requirement is to remove any rows that contain null cells).
    sales_data = list(filter(lambda row: '' not in row.values(), sales_data))

    # Optional / Stretch goals
    # 3. Filter data for the period 1 December 2020 - 5 December 2020
    start_date = datetime.strptime("2020-12-01", '%Y-%m-%d')
    end_date = datetime.strptime("2020-12-05", '%Y-%m-%d')
    sales_data = [row for row in sales_data if datetime.strptime(row['purchase_date'], '%Y-%m-%d') >= start_date and datetime.strptime(row['purchase_date'], '%Y-%m-%d') <= end_date]
    
    # 4. Calculate each customer's total spend
    # 5. Calculate each customer's average spend
    # 6. Calculate how many times each customer has purchased a specific item


    ### SETUP THE DATABASE CONNECTION
    print('Opening connection...')
    conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
    # Establish a database connection
    with psycopg2.connect(conn_string) as connection:

        print('Opening cursor...')
        cursor = connection.cursor()

        ### Task 1.3 - LOAD
        # 7. Load the transformed data to the created tables
        # TODO - put code here to insert into the tables
        sql = """
            INSERT INTO sales_data (customer_id, purchase_date, purchase_amount, product_id)
            VALUES (%s, %s, %s, %s)
            RETURNING customer_id;
        """
        for row in sales_data:
            print(row)    
            data_values = tuple(row.values())
            cursor.execute(sql, data_values)
        print('Closing cursor...')
        # Closes the cursor so will be unusable from this point
        cursor.close()

        # The connection will automatically close here
except Exception as ex:
    print('Failed to:', ex)

# Leave this line here!
print('All done!')
