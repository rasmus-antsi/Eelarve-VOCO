from django.db import models
import uuid
# Create your models here.
class transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField()
    description = models.TextField(max_length=255)
    date = models.DateField()
    category = models.CharField(max_length=255)
    is_income = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description