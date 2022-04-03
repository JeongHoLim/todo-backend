from typing import ItemsView
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'urls',views.ItemViewSet,basename="urls")

urlpatterns = [
    path('item',views.ItemList.as_view()),
    path('item/<int:pk>',views.ItemDetail.as_view())
]