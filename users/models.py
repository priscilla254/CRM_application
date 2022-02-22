from django.db import models
from django.contrib.auth.models import  AbstractUser



class User(AbstractUser):
    pass

class Agent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # first_name=models.CharField(max_length=80)
    # last_name=models.CharField(max_length=80)
    def __str__(self):
        return self.user.username

# class Lead(models.Model):
#     first_name=models.CharField(max_length=80)
#     last_name=models.CharField(max_length=80)
#     Company=models.CharField(max_length=80)
#     company_position=models.CharField(max_length=80)
#     phone_number=models.IntegerField(default=0)
#     email_address=models.EmailField()
#     agent=models.ForeignKey(Agent,on_delete=models.SET_NULL,null=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"