from django.contrib import admin
from django.urls import path
from test1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('stuinfo/<int:ip>', views.get_student_detail),
    #path('stuinfo/', views.get_student_list),
    #path('stusave/', views.post_student),
    path('api/', views.api),
]
