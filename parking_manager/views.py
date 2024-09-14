from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement
from .serializers import CustomerSerializer, VehicleSerializer, PlanSerializer, CustomerPlanSerializer, ContractSerializer, ContractRuleSerializer, ParkMovementSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class CustomerPlanViewSet(viewsets.ModelViewSet):
    queryset = CustomerPlan.objects.all()
    serializer_class = CustomerPlanSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class ContractRuleViewSet(viewsets.ModelViewSet):
    queryset = ContractRule.objects.all()
    serializer_class = ContractRuleSerializer

class ParkMovementViewSet(viewsets.ModelViewSet):
    queryset = ParkMovement.objects.all()
    serializer_class = ParkMovementSerializer
