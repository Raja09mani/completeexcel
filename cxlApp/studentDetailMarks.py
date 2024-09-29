from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

def get_student_with_marks(sql_query):
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        print(">>>",cursor)
        print(cursor.description)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    # Convert rows to a list of dictionaries
    data_list = [dict(zip(columns, row)) for row in rows]

    return data_list