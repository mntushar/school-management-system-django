from django.db import models


#teacher information table
class TeacherInfo(models.Model):
    name = models.CharField(max_length=50, blank=True, unique=True)
    gender_choice = [
        ('male', 'Male'),
        ('female', 'Female'),
    ] 
    gender = models.CharField(
        max_length=6,
        blank=True,
        choices=gender_choice,
    )
    phonenumber = models.IntegerField(blank=True)
    designation = models.CharField(max_length=150, blank=True)




