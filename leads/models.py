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

class Contact(models.Model):
    name=models.CharField(max_length=100)
    account_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=80)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Opportunity(models.Model):
    stage_choices=(
        ('qualification','qualification'),
        ('needs analysis','needs analysis'),
        ('proposal','proposal'),
        ('negotiation','negotiation'),
        ('closed won','closed won'),
        ('closed lost','closed lost')
    )
    opportunity_name=models.CharField(max_length=100)
    account_name=models.CharField(max_length=80)
    stage=models.CharField(choices=stage_choices,max_length=80)
    close_date=(models.DateField(auto_now_add=True))
    opportunity_owner=models.CharField(max_length=80)