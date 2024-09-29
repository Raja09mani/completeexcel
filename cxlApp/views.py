from rest_framework import viewsets
from .models import StudentDetail, StudentMark,StudDetail
from .serializers import StudentDetailSerializer, StudentMarkSerializer, StudDetailSerializer
from .models import StudentDetail, StudentMark
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .studentDetailMarks import get_student_with_marks  # Make sure to import the method
from django.shortcuts import get_object_or_404
from rest_framework import status
import pandas as pd
from django.http import JsonResponse
from .process_uploaded import process_uploaded_files
from .thirdparty import call_third_party_api
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .auth import create_jwt_token

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        print("hi")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            token = create_jwt_token({'id': user.id, 'username': user.username})
            print(token)
            return JsonResponse({'token': token})
        else:   
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'POST request required'}, status=400)

@api_view(['GET'])

def protected_view(request):
    if request.user_payload:
        return JsonResponse({'message': 'This is a protected view.', 'user_payload': request.user_payload})
    return JsonResponse({'error': 'Unauthorized'}, status=401)

class StudentDetailViewSet(viewsets.ModelViewSet):
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer

class StudentMarkViewSet(viewsets.ModelViewSet):
    queryset = StudentMark.objects.all()
    serializer_class = StudentMarkSerializer

@api_view(['POST'])
def test(request):
    print("hello")
    #queryset = StudentDetail.objects.values()
    my_object = StudentDetail.objects.create(sid=request.data["sid"],sno=request.data["sno"],sname=request.data["sname"],sclass=request.data["sclass"],saddress=request.data["saddress"])
    print(my_object)
    
@api_view(['GET'])
def get_view(request):
    
    # Get the student detail object
    print(request.data)
    print('hello')
    search_value= request.data['name']
    
    query = f'''SELECT sd.*, sm.*
            FROM public."studApp_studentdetail" AS sd
            LEFT JOIN public."studApp_studentmark" AS sm ON sd.sid = sm.roll_id
            WHERE sd.sname LIKE '{search_value}%' '''
            
    result = get_student_with_marks(query)
    return Response(result)

@api_view(['POST'])
def update_database(request):
    # Check if a file is provided in the request
    print(request.FILES)
    if 'file.xlsx' not in request.FILES:
        return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

    # Get the uploaded file
    excel_file = request.FILES['file.xlsx']

    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Convert DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')


    # Update or create database entries
    for record in data:
        students = StudDetail.objects.filter(roll=record.get("roll"))
        print(students)
        
        if students.exists():
            students.update(
            roll=record.get('roll'),
            sname=record.get('sname'),
            sclass= record.get('sclass'),
            saddress= record.get('saddress'),
            tamil= record.get('tamil'),
            english= record.get('english'),
            maths= record.get('maths'),
            science= record.get('science'),
            socialscience= record.get('socialscience'),
            )
        else:
            StudDetail.objects.create(
            roll=record.get('roll'),
            sname=record.get('sname'),
            sclass= record.get('sclass'),
            saddress= record.get('saddress'),
            tamil= record.get('tamil'),
            english= record.get('english'),
            maths= record.get('maths'),
            science= record.get('science'),
            socialscience= record.get('socialscience'),
            )

    return Response({"status": "success"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def update_database_header(request):
    try:
        # Ensure the file key matches the form field name ('file' instead of 'file.xlsx')
        uploaded_files = request.FILES.getlist('file.xlsx')

        if not uploaded_files:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Call the utility function to process the uploaded files
        responses = process_uploaded_files(uploaded_files)
        
        return JsonResponse({"responses": responses})
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def call_api_view(request):
    if request.method == 'POST':
        data = request.data  # Automatically parses JSON data
        response_data, status_code = call_third_party_api(data)
        return Response(response_data, status=status_code)

    return Response({'error': 'Invalid request method'}, status=400)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .weather import call_weather_api

@api_view(['POST'])
def api_view(request):
    if request.method == 'POST':
        data = request.data  # Automatically parses JSON data
        response_data, status_code = call_weather_api(data)
        return Response(response_data, status=status_code)

    return Response({'error': 'Invalid request method'}, status=400)

# views.py

from django.http import JsonResponse

from cxlApp.extractDownload import extract_data, save_to_excel
from rest_framework.decorators import api_view
@api_view(['POST'])
def download_data(request):
    if request.method == 'POST':
        # Define your SQL query
        #search_value= request.data['name']
        sql_query = 'SELECT * FROM public."studApp_studentdetail"'
            
        #sql_query = "YOUR RAW SQL QUERY HERE"

        # Step 2: Extract data using raw SQL
        rows, columns = extract_data(sql_query)
        
        # Step 3: Use pandas to create an Excel file
        file_path = r'C:\Users\raja0\OneDrive\Desktop\Dowload data as excel/extracted_data.xlsx'
        save_to_excel(rows, columns, file_path)

        # Step 5: Return the file path in the response
        return JsonResponse({'file_path': file_path})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

