from django.urls import path,include
from .import views 
urlpatterns = [
    path('',views.home,name="homepage"),
    
    path('edit/<int:roll>/', views.edit_student, name='edit_student'),
    path('delete/<int:roll>/', views.delete_student, name='delete_student'),
    
]