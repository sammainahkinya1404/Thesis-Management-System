from django.db import models
from users.models import CustomUser

class Thesis(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255)
    abstract = models.TextField()
    file = models.FileField(upload_to='theses/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    feedback = models.TextField(blank=True, null=True)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='theses')
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_theses',
        limit_choices_to={'role': 'teacher'},  # Only teachers appear in the dropdown
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (by {self.student.username})"



class ThesisProgress(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name='progress')
    milestone = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.thesis.title} - {self.milestone}"
