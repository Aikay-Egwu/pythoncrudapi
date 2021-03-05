from django.db import models

# Create your models here.
class Student(models.Model):
  firstname = models.CharField(max_length=100, null=False, blank=False)
  surname = models.CharField(max_length=100, null=False, blank=False)
  gender = models.CharField(max_length=1, null=False, blank=False)
  age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.firstname
