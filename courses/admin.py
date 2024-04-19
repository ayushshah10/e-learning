from django.contrib import admin
from .models import Enrollment,Course,Comment,Topic,Review
# Register your models here.

admin.site.register(Enrollment)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(Review)
