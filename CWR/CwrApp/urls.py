from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api
app_name = 'CwrApp'
router = DefaultRouter()
router.register(r'chat', api.MessagesAreaModelViewSet, basename='api-chats')
urlpatterns = [
   path('', views.index, name='index'),
   path('signup/', views.signupHandle, name='signup'),
   path('login/', views.loginHandle, name='login'),
   path('logout/', views.logoutHandle, name='login'),
   path('submit/', views.submit, name='submit'),
   path(r'api/', include(router.urls)),
]
