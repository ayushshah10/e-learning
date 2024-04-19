from rest_framework import serializers
from .models import Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
    def create(self,data):
        course = Course.objects.create(
            title = data['title'],
            description = data['description'],
            price = data['price'],
            course_length = data['course_length'],
            domain = data['domain']
        )
        
        course.save()
        return course
