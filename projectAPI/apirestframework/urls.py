from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    # default
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # custome
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # URL
    path('user/', UserList.as_view(), name='user_list'),
    path('register/', UserRegist.as_view(), name='register'),
    path('genre_create/', CreateGenre.as_view(), name='genre_create'),
    path('genre_list/', GenreList.as_view(), name='genre_list'),
    path('genre_update/<int:pk>', GenreUpdate.as_view(), name='genre_update'),
    path('genre_delete/<int:pk>', GenreDelete.as_view(), name='genre_delete'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]