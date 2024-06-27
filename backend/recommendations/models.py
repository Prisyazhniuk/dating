from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    recommended_user = models.ForeignKey(User, related_name='recommended_to', on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f'Recommendation from {self.user} to {self.recommended_user} with score {self.score}'
