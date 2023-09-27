from rest_framework import viewsets
from .models import Image, AccountTier
from .serializers import ImageSerializer, AccountTierSerializer
from django.shortcuts import render
from django.http import JsonResponse


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class AccountTierViewSet(viewsets.ModelViewSet):
    queryset = AccountTier.objects.all()
    serializer_class = AccountTierSerializer


# def upload_image(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         image = request.FILES['image']
#         # Process the uploaded image here (e.g., save it to the media directory)
#         # ...
#
#         return JsonResponse({'message': 'Image uploaded successfully.'})
#
#     return JsonResponse({'message': 'No image found in the request.'})
