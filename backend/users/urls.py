from django.contrib import admin
from django.urls import path
from .views import UserAPIView

urlpatterns = [
    path('',UserAPIView.as_view({'get':'list'})),
    path('add/', UserAPIView.as_view({'post':'create'})),
    path('<int:pk>', UserAPIView.as_view({'post':'update'})),
    path('<int:pk>', UserAPIView.as_view({'delete':'destroy'})),
    path('<int:pk>',UserAPIView.as_view({'get':'retrieve'})),
    path('', admin.site.urls),
]
