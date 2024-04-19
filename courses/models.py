from django.db import models
from core.models import CustomUser
from django.core.exceptions import ValidationError

def isInRange(value):
    if value<1 and value>10:
        raise ValidationError('rating must be in 1 to 10',params={'value':value})

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    rating = models.IntegerField(editable=False)
    course_length = models.IntegerField()
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    domain_field = models.CharField(max_length=100)
    
    READ_ONLY_FIELDS = [created_at,modified_at]
    class Meta:
        ordering = ('-created_at',)
        
    
    def __str__(self):
        return self.title
    
    
class Topic(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='files/')
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    video_id = models.ForeignKey(Topic,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[isInRange])


class Comment(models.Model):
    video = models.ForeignKey(Topic,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()


class Enrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    enrolled_at = models.DateField(auto_now_add=True)