from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, UserViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path("", include(router.urls))
]