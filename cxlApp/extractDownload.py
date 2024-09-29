# utils.py

import pandas as pd
from django.db import connection

def extract_data(query):
    """
    Extracts data from the database using a raw SQL query.
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
    return rows, columns

def save_to_excel(data, columns, file_path):
    """
    Saves data to an Excel file.
    """
    df = pd.DataFrame(data, columns=columns)
    print(df)
    df.to_excel(file_path, index=False)
