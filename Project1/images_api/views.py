from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you're at the images_api index")
