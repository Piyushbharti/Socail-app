from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from userAuth import views
from blogs import views
from employees.views import EmployeeOperation

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/register', views.register),
    # path('api/v1/alluser', views.getAllUser),
    # path('api/v1/user/<int:pk>/', views.studentDetailView),
    # path('api/v1/updateUser/<int:pk>', views.updateCoustomerDetails),
    # path('api/v1/deleteUser/<int:pk>', views.deleteUser)
    # path('api/v1/allUserByClass', views.Employees.as_view()),
    # path('api/v1/allUser/update/<int:pk>', views.EmployeeDetails.as_view()),
    # path('api/v1/allmixin', views.EmployeeDetails.as_view())
    # path('api/v1/employee', views.list)
    path('api/v1/blog', views.BlogOperations.as_view()),
    path('api/v1/comment', views.commentOperations.as_view()),
    path('api/v1/blog/<int:pk>/', views.getBlogById),
    # path('api/v1/blog/<int:pk>/', views.BlogDetailView.as_view()),
    path('api/v1/comment/<int:pk>/', views.commentDetailView.as_view()),
    path('api/v1/employee', EmployeeOperation.as_view()),
    # path('api/v1/alluserByClass/<int:pk>/', views.coustomerDetails.as_view()),
]
