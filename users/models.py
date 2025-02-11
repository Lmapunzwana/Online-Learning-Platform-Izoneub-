from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLES = (
        ('ADMIN','ADMIN'),
        ('LEARNER','LEARNER'),
        ('INSTRUCTOR','INSTRUCTOR')
    )
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    role      = models.CharField(max_length=20, choices=ROLES, default='INSTRUCTOR')
    full_name = models.CharField(max_length=255, null=True, blank=True)
    country   = models.CharField(max_length=255, null=True, blank=True)
    city      = models.CharField(max_length=255, null=True, blank=True)
    zip_code  = models.CharField(max_length=255, null=True, blank=True)
    address   = models.CharField(max_length=255, null=True, blank=True)
    dob       = models.DateField(max_length=30,blank=True,null=True)
    phone     = models.CharField(max_length=255, null=True, blank=True)
    avatar    = models.ImageField(upload_to='avatar/', null=True, blank=True,default="avatar/default.webp")


# class CourseProgress(models.Model):
#     STATUSES = (
#         ('active','active'),
#         ('enrolled','enrolled'),
#         ('completed','completed')
#     )
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     # course = models.ForeignKey(Course,on_delete=models.CASCADE)
#     status = models.CharField(max_length=15,default='active',choices=STATUSES)

