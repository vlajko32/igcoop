from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'expert-reports', ExpertReportViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'machine-values', MachineValueViewSet)

urlpatterns = router.urls
