from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TipCalculator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bill = models.DecimalField(max_digits=10, decimal_places=2)
    tip_percentage = models.IntegerField()
    people = models.IntegerField()
    total_bill = models.DecimalField(max_digits=10, decimal_places=2)
    per_person = models.DecimalField(max_digits=10, decimal_places=2)
    calculated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calculation by {self.user if self.user else 'Anonymous'} on {self.calculated_at}"
