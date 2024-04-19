from django.shortcuts import render,redirect
from rest_framework.views import APIView,Response
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not CustomUser.objects.filter(email=email).exists():
            messages.error(request,'User does not exists!')
            return redirect('login')
        else:
            user = authenticate(request,email=email,password=password)
            print(user,email,password)
            if user is None:
                messages.error(request,'Wrong Password!')
                return redirect('login')
            login(request,user)
            token,_ = Token.objects.get_or_create(user=user)
            return redirect('home')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

class RegisterView(APIView):
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response({
                'errors':serializer.errors,
                'status':400})
        serializer.save()
        
        return redirect('login')
    

