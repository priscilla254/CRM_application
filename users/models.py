from django.db import models

class Agent(models.Model):
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)


class Lead(models.Model):
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    Company=models.CharField(max_length=80)
    company_position=models.CharField(max_length=80)
    phone_number=models.IntegerField(default=0)
    email_address=models.EmailField()
    agent=models.ForeignKey(Agent,on_delete=models.SET_NULL,null=True)
