from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement
from .serializers import CustomerSerializer, VehicleSerializer, PlanSerializer, CustomerPlanSerializer, ContractSerializer, ContractRuleSerializer, ParkMovementSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    @action(detail=False, methods=['get'])
    def parked(self, request):
        # Filtra os veículos que têm parkmovement.exit_date nulo e entry_date não nulo
        vehicles = Vehicle.objects.filter(
            parkmovement__exit_date__isnull=True,
            parkmovement__entry_date__isnull=False
        ).prefetch_related('parkmovement_set').select_related('customer')
        
        # Adiciona entry_date ao serializer
        serializer = self.get_serializer(vehicles, many=True)
        for index, vehicle in enumerate(vehicles):
            entry_date = vehicle.parkmovement_set.first().entry_date if vehicle.parkmovement_set.exists() else None
            if entry_date:
                # Formata a data para dia/mês/ano - horário
                entry_date = entry_date.strftime("%d/%m/%Y - %H:%M")
            serializer.data[index]['entry_date'] = entry_date
        
        # Retorna a resposta com os dados serializados
        return Response(serializer.data)

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
