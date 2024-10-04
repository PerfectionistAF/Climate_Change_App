##STEP 1: admin/major api functionality, main API registry
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from climate_story.api.urls import emissions_router

router= DefaultRouter()  ##main router

#app1
#app2

#emissions app
router.registry.extend(emissions_router.registry)

urlpatterns = [
    path('', include(router.urls)),  ##router.urls

]


##include urls here in the core urls file------> core/core/urls.py