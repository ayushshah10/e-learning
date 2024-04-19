
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout')
]
