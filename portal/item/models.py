from django.db import models
from django.contrib.auth.models import User




class Department(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    

class Item(models.Model):
    department=models.ForeignKey(Department, related_name='department_items', on_delete=models.CASCADE)
    job_category=models.ForeignKey(Category, related_name='category_items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True, null=True)
    available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField()
    requirement=models.TextField(blank=True, null=True)
    duties=models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='user_items', on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name_plural = 'Items'
    
    def __str__(self):
        return self.name