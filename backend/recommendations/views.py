from rest_framework import generics
from users.models import CustomUser  # Импортируем CustomUser вместо User
from .serializers import UserSerializer

class RecommendationsView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        # Логика для получения рекомендаций на основе интересов пользователя
        # Например, использовать алгоритмы машинного обучения для рекомендаций
        return super().get_queryset().exclude(id=user.id)
