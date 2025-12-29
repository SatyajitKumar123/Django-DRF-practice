from django.conf import settings
from django.db import models 

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="expense"
    )
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=False)
    is_recurring = models.BooleanField(default=False)
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', '-expense_date'])
        ]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(amount__gt=0),
                name="amount_positive"
            )
        ]
        
    
    def __str__(self):
        return f"{self.user} - {self.amount}"

    def is_high_value(self):
        return self.amount > 5000