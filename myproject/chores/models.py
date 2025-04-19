from django.db import models
from users.models import UserProfile

# Create your models here.
class ChoreDefinition(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class ChoreInstance(models.Model):
    chore = models.ForeignKey(ChoreDefinition, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    assignment_date = models.DateField()
    completed_at = models.TimeField()
    
    def __str__(self):
        return f"${self.chore.title} - ${self.assignment_date}"