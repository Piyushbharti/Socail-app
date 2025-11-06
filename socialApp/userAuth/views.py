from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from userAuth.serializer import AuthSerializer
from userAuth.models import coustomerUser

@csrf_exempt
@api_view(['POST'])
def register(req):
    name = req.data.get('name')
    password = req.data.get('password')
    
    if not name or not password:
        return Response({"error": "Name and password not provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        print(req.data)
        serializer = AuthSerializer(data=req.data)  # <-- fix here
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print('Something went wrong:', e)
        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def getAllUser(request):
    try:
        allUser = coustomerUser.objects.all()
        serializer = AuthSerializer(allUser, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print('Something went wrong:', e)
        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET'])
def studentDetailView(request, pk):
    try:
        student = coustomerUser.objects.get(pk=pk)
    except coustomerUser.DoesNotExist:
        return Response({"message" : "Data Does not exist"},status=status.HTTP_400_BAD_REQUEST)
    serializer = AuthSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def updateCoustomerDetails(request, pk):
    try:
        student = coustomerUser.objects.get(pk=pk)
    except coustomerUser.DoesNotExist:
        return Response({"message" : "Data Does not exist"},status=status.HTTP_400_BAD_REQUEST)
    serializer = AuthSerializer(student, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    