from django.contrib import admin
from .models import Customer, Vehicle, Plan, Contract, CustomerPlan, ContractRule, ParkMovement
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Plan)
admin.site.register(Contract)
admin.site.register(CustomerPlan)
admin.site.register(ContractRule)
admin.site.register(ParkMovement)
