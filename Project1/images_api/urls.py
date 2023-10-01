from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, AccountTierViewSet
from .views import upload_image
# from django.contrib import admin
# from . import views


app_name = 'images_api'

router = DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'account-tiers', AccountTierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', upload_image, name='upload_image'),

]


# urlpatterns = [
#     path('', views.index, name='index'),
# ]
