from rest_framework import viewsets
from .models import Image
from .models import AccountTier
from .serializers import ImageSerializer, AccountTierSerializer
from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image as PILImage
from utils import generate_links
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


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


def generate_links_view(request):
    # Get the currently logged-in user
    user = request.user

    # Get the image URL from the request or any other source
    image_url = request.GET.get('image_url')

    # Generate the links based on the user's account tier
    links = generate_links(user, image_url)

    # Pass the links to the template or return them in the response
    return render(request, 'generate_links.html', {'links': links})


def generate_expiring_link(image_url, expiration_time):
    parsed_url = urlparse(image_url)
    query_params = parse_qs(parsed_url.query)
    query_params['expires'] = [(datetime.now() + timedelta(seconds=expiration_time)).isoformat()]
    updated_query_string = urlencode(query_params, doseq=True)
    updated_url = urlunparse(parsed_url._replace(query=updated_query_string))
    return updated_url
