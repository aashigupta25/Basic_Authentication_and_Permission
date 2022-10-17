from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating default Router Objects
router = DefaultRouter()

# Register PersonViewset with router
router.register('personapi', views.PersonModelViewset, basename='Person')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
