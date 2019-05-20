from django.urls import path
from fiddle1 import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/<int:id>', views.employee_detail)
]
