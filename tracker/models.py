# tracker/models.py
from django.db import models

class Bug(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    # ▼▼▼ ADD/CHECK THESE LINES FOR STATUS ▼▼▼
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )
    # ▲▲▲ ADD/CHECK THESE LINES FOR STATUS ▲▲▲

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    def __str__(self):
        return self.title