from django.urls import path
from . import views
urlpatterns = [
    path('',views.CourseView.as_view(),name='courses'),
    path('addcourse',views.AddCourse.as_view(),name='add_course'),
    path('myuploads/',views.CourseById.as_view(),name='coursebyid'),
]