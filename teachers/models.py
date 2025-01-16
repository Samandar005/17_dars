from django.db import models
from subjects.models import Subject
from django.shortcuts import reverse
from teachers.base_models import BaseModel


class Teacher(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers', null=True)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    work_experience = models.PositiveIntegerField(default=0)
    images = models.ImageField(upload_to='photos/', blank=True, null=True)

    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"