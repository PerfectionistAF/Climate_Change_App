##STEP 3: create urls for api, rest framework
from rest_framework.routers import DefaultRouter
from .views import EmissionsViewSet

emissions_router = DefaultRouter()

##path for url route for the model
##aliasing
emissions_router.register(r'emissions', EmissionsViewSet)#, basename='emissions')

