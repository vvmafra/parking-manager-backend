from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    card_id = models.CharField(max_length=10, null=True, blank=True)

class Vehicle(models.Model):
    plate = models.CharField(max_length=10)
    model = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)

class Plan(models.Model):
    description = models.CharField(max_length=50)
    value = models.FloatField()

class CustomerPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True)

class Contract(models.Model):
    description = models.CharField(max_length=50)
    max_value = models.FloatField(null=True, blank=True)

class ContractRule(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    until = models.IntegerField()
    value = models.FloatField()

class ParkMovement(models.Model):
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField(null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True)
