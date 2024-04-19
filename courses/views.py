from django.shortcuts import render,redirect
from rest_framework.views import APIView,Response
from .models import Course,Topic
from .serializers import CourseSerializer
from django.contrib.auth.decorators import login_required

class CourseView(APIView):
    def get(self,request):
        return render(request,'courses.html')

    
class SingleCourse(APIView):
    def get(self,request,id):
        course = Course.objects.get(id=id)
        context = {
            'course':course
        }

        return render(request,'singlecourse.html',context)

class CourseById(APIView):
    def get(self,request):
        items = Course.objects.filter(created_by = self.request.user)
        context = {
            'items':items
        }
        return render(request,'myuploads.html',context)

class AddCourse(APIView):
    def get(self,request):
        return render(request,'courseform.html')
    

    @login_required(login_url='login')
    def post(self,request):
        serializer = CourseSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({
            'errors':serializer.errors,
            'status':400})
        serializer.save()
        return redirect('home')


class TopicByCourse(APIView):
    def get(self,request,id):
        topics = Topic.objects.get(course__id = id)
        context = {
            'topics':topics
        }
        return render(request,'singlecourse.html',request)