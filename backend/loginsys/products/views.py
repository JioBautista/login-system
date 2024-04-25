from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    BasePermission,
)
from .models import Products
from .serializers import ProductSerializer


class isManager(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Managers").exists()
        )


class isClerk(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name="Clerks").exists()
        )


class ProductsList(ListCreateAPIView):
    permission_classes = [isManager | isClerk]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [isManager]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
