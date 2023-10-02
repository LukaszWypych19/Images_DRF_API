from .models import Plan
from views import generate_thumbnail, generate_expiring_link

def generate_links(user, image_url):
    links = []

    # Generate link to a thumbnail that's 200px in height
    thumbnail_200px = generate_thumbnail(image_url, height=200)
    links.append(thumbnail_200px)

    # Check the user's account tier
    if user.plan == Plan.PREMIUM or user.plan == Plan.ENTERPRISE:
        # Generate link to a thumbnail that's 400px in height
        thumbnail_400px = generate_thumbnail(image_url, height=400)
        links.append(thumbnail_400px)

        # Generate link to the originally uploaded image
        links.append(image_url)

    # Check if the user has an Enterprise plan
    if user.plan == Plan.ENTERPRISE:
        # Generate an expiring link to the image
        expiration_time = 600  # Default expiration time in seconds
        # You can allow the user to specify the expiration time and validate it
        # expiration_time = user_specified_expiration_time
        expiring_link = generate_expiring_link(image_url, expiration_time)
        links.append(expiring_link)

    return links
