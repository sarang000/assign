from django.db import models

# Create your models here.

class AdminLoginPage(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=8)

class organisationRegistration(models.Model):
    date = models.DateField()
    organsation_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    organsation_address = models.CharField(max_length=500)
    branch_id = models.IntegerField(default=5)
    branch_code =models.CharField(max_length=50)
    password =models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)

class AdminBranch(models.Model):
    date = models.DateField()
    branch_id = models.IntegerField(default=5)
    branch_name = models.CharField(max_length=50)
    branch_code =models.CharField(max_length=50)
    branch_address = models.CharField(max_length=50)
    branch_location = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=50)

class AdminOrgModifi(models.Model):
    date = models.DateField()
    organisation_name =models.CharField(max_length=50)
    branch =models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    branch_id = models.IntegerField(default=5)
    branch_code =models.IntegerField(default=5)
    password = models.CharField(max_length=50)
    repeat_password=models.CharField(max_length=50)


class AdminAgentDetails(models.Model):
    agent_id =models.IntegerField(default=5)
    agent_name =models.CharField(max_length=50)
    father_name =models.CharField(max_length=50)
    age =models.IntegerField(default=5)
    sex =models.CharField(max_length=50)
    occupation =models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    password =models.CharField(max_length=50)
    repeat_password =models.CharField(max_length=50)


class CompanyOfficals(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
    id=models.IntegerField(default=5,primary_key=True)

class CompanyOrgRegistration(models.Model):
    date = models.DateField()
    organsation_name =models.CharField(max_length=10)
    branch_id = models.IntegerField(default=5)
    branch_name = models.CharField(max_length=10)
    branch_code = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    password = models.CharField(max_length=10)
    repeat_password = models.CharField(max_length=10)
class CompanyPolicyRegistration(models.Model):
    date = models.DateField()
    policy_name = models.CharField(max_length=50)
    policy_Amount = models.IntegerField(default=10)
    interest = models.IntegerField(default=10)
    bonus_rate = models.IntegerField(default=10)
    policy_team = models.CharField(max_length=50)
    bonus_period = models.CharField(max_length=50)
    policy_expiry_date=models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    repeat_password = models.CharField(max_length=8)


class Agent(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
    id=models.IntegerField(default=5,primary_key=True)

class Customer(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    id = models.IntegerField(default=5, primary_key=True)


