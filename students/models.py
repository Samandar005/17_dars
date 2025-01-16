from django.db import models
from django.shortcuts import reverse
from groups.models import Group
from teachers.base_models import BaseModel


class Student(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students', null=True)
    birth_date = models.DateField()
    images = models.ImageField(upload_to='i mages/')
    phone_number = models.CharField(max_length=13)
    address = models.TextField()

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
