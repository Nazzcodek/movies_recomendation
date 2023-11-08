from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateUserView, ModifyUserView, UserViewSet, login

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('profile/', ModifyUserView.as_view(), name='modify_user_profile'),
    path('login/', login, name='login'),
    path('', include(router.urls)),
]
