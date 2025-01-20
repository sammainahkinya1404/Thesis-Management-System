from django.db import models
from theses.models import Thesis

class Grade(models.Model):
    thesis = models.OneToOneField(Thesis, on_delete=models.CASCADE, related_name='grade')
    score = models.DecimalField(max_digits=5, decimal_places=2)  # Score out of 100
    feedback = models.TextField()
    graded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.thesis.title} - {self.score}"
