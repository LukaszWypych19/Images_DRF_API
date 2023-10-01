from rest_framework import viewsets
from .models import Image
from .models import AccountTier
from .serializers import ImageSerializer, AccountTierSerializer
from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image as PILImage


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class AccountTierViewSet(viewsets.ModelViewSet):
    queryset = AccountTier.objects.all()
    serializer_class = AccountTierSerializer


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Process the uploaded image here (e.g., save it to the media directory)
        # ...

        # Generate the thumbnail
        thumbnail = generate_thumbnail(image)

        return JsonResponse({'message': 'Image uploaded successfully.', 'thumbnail_url': thumbnail.url})

    return JsonResponse({'message': 'No image found in the request.'})


def generate_thumbnail(image):
    # Open the uploaded image using PIL
    img = PILImage.open(image)

    # Calculate the aspect ratio
    width, height = img.size
    aspect_ratio = width / height

    # Calculate the new width based on the desired height of the thumbnail
    new_width = int(200 * aspect_ratio)

    # Resize the image to the new dimensions
    img.thumbnail((new_width, 200))

    # Save the thumbnail to a new file
    thumbnail_path = f'media/thumbnails/{image.name}'
    img.save(thumbnail_path)

    return thumbnail_path
