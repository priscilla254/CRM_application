from django.db import models
from users.models import Agent
class Lead(models.Model):
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    company=models.CharField(max_length=80)
    company_position=models.CharField(max_length=80)
    phone_number=models.CharField(max_length=80,unique=True)
    email_address=models.EmailField()
    agent=models.ForeignKey(Agent,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
