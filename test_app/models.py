from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True, error_messages={
        'null': 'This is an error message'
    })
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_alive = models.BooleanField()
    amount = models.FloatField()
    extra_name = models.CharField(max_length=200, editable=False, default='null')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Test Model'
    
    
    def save(self, *args, **kwargs):
        self.extra_name = f"{self.name} - {self.phone_number}"
        return super().save(*args, **kwargs)


class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name='test_content')
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'ModelX'

    
    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"