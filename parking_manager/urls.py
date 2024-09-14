from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, VehicleViewSet, PlanViewSet, CustomerPlanViewSet, ContractViewSet, ContractRuleViewSet, ParkMovementViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'customerplans', CustomerPlanViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'contractrules', ContractRuleViewSet)
router.register(r'parkmovements', ParkMovementViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
