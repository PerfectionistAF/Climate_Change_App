##STEP 1: admin/major api functionality
from rest_framework.router import DefaultRouter
from django.urls import path, include
from climate_story.api.urls import emissions_router

router= DefaultRouter()

#app1
#app2

#emissions app
router.registry.extend(emissions_router.registry)
urlpatterns = [
    path('', include(router.urls)),  ##router.urls

]