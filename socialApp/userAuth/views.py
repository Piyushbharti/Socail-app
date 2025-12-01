from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from userAuth.serializer import AuthSerializer
from userAuth.models import coustomerUser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics, viewsets

# @csrf_exempt
# @api_view(['POST'])
# def register(req):
#     name = req.data.get('name')
#     password = req.data.get('password')
    
#     if not name or not password:
#         return Response({"error": "Name and password not provided"}, status=status.HTTP_400_BAD_REQUEST)
    
#     try:
#         print(req.data)
#         serializer = AuthSerializer(data=req.data)  # <-- fix here
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         print('Something went wrong:', e)
#         return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    
    
# @api_view(['GET'])
# def studentDetailView(request, pk):
#     try:
#         student = coustomerUser.objects.get(pk=pk)
#     except coustomerUser.DoesNotExist:
#         return Response({"message" : "Data Does not exist"},status=status.HTTP_400_BAD_REQUEST)
#     serializer = AuthSerializer(student)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['PUT'])
# def updateCoustomerDetails(request, pk):
#     try:
#         student = coustomerUser.objects.get(pk=pk)
#     except coustomerUser.DoesNotExist:
#         return Response({"message" : "Data Does not exist"},status=status.HTTP_400_BAD_REQUEST)
#     serializer = AuthSerializer(student, data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# @api_view(['DELETE'])
# def deleteUser(request, pk):
#     try:
#         student = coustomerUser.objects.get(pk=pk)
#     except coustomerUser.DoesNotExist:
#         return Response({"message": "Data Does not exist"}, status=status.HTTP_400_BAD_REQUEST)
#     student.delete()
#     return Response(status=status.HTTP_200_OK)
     
# class coustomer(APIView):
#     def get(self, request):
#         alldata = coustomerUser.objects.all()
#         serializer = AuthSerializer(alldata, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         data = AuthSerializer(data = request.data)
#         if data.is_valid():
#             data.save()
#             return Response('Data save success', status.HTTP_201_CREATED)
      
# class coustomerDetails(APIView):
#     def getObject(self, pk):
#         try:
#             data = coustomerUser.objects.get(pk = pk)
#             return data
#         except:
#             return Http404
#     def get(self, request, pk):
#         employee = self.getObject(pk)
#         serializer = AuthSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         coustomer = self.getObject(pk)
#         serializer = AuthSerializer(coustomer, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk):
#         serializer = coustomerUser.objects.get(pk=pk)
#         serializer.delete()
#         return Response('User delete success')


# Mixins
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = coustomerUser.objects.all()
#     serializer_class = AuthSerializer
    
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
    
# class EmployeeDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = coustomerUser.objects.all()
#     serializer_class = AuthSerializer
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#     def put(self, request, pk):
#         return self.update(request, pk)
#     def delete(self, request, pk):
        # return self.destroy(request, pk)
        
        
# Generic Views
# class Employees(generics.ListCreateAPIView):
#     queryset = coustomerUser.objects.all() # isme v queryset likhna jaruri
#     serializer_class = AuthSerializer   # serializer_class likhna jaruri h


# class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = coustomerUser.objects.all() # isme v queryset likhna jaruri
#     serializer_class = AuthSerializer # serializer_class likhna jaruri h
#     lookup_field = 'pk' # lookup_field likhna jaruri h
    
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = AuthSerializer.objects.all()
        return Response(serializer.data)
    
@api_view(['GET'])
def getAllUser(request):
    try:
        allUser = coustomerUser.objects.all()
        serializer = AuthSerializer(allUser, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print('Something went wrong:', e)
        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = AuthSerializer.objects.all()
        return Response(serializer.data)