from django.urls import path

# Local Application Imports
from user.views import UserViewSet, UserSingleViewSet

app_name = 'user'

urlpatterns = [
    path('user/',UserViewSet.as_view(),name='users'),
    path('user/<int:pk>',UserSingleViewSet.as_view(),name='user')
]
