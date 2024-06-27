from rest_framework import serializers
from users.models import CustomUser  # Импортируем CustomUser вместо User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'interests']
