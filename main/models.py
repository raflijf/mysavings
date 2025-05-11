from django.db import models
from django.utils.text import slugify
from account.models import User
from decimal import Decimal


# Create your models here.
class Saving(models.Model) : 
    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name='saving')
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=270, blank=True)
    target = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    collected = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    deadline = models.DateField(auto_now=False, null=True, blank=True)
    # link = 
    slug = models.SlugField(blank=True)

    def save(self) :
        self.slug = slugify(self.title)
        return super().save()

    class Meta : 
        db_table = 'saving'

    def __str__(self):
        return self.title
    

class SavingLogs(models.Model) :
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE, related_name='saving_entries')
    nominal = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    description = models.TextField(max_length=270, blank=True)
    status = models.CharField(max_length=7)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta : 
        db_table = 'saving_logs'