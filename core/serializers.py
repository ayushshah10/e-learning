from rest_framework import serializers
from .models import CustomUser
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    # def create_user(self,data):

    def create(self,data):
        user = CustomUser.objects.create(
            username = data['username'],
            email = data['email'],
            password = data['password'],
            phone_no = data['phone_no'],
        )
        
        user.set_password(data['password'])
        user.save()
        print('in create')
        return user