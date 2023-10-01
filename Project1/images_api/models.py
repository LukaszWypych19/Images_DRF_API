from django.db import models
from django.contrib.auth.models import User


class AccountTier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.CharField(max_length=255)
    show_original_link = models.BooleanField(default=False)
    generate_expiring_link = models.BooleanField(default=False)
    link_expiration_time = models.PositiveIntegerField(
        default=300,
        help_text='Link expiration time in seconds (300 - 30000)'
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    account_tier = models.ForeignKey(AccountTier, on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.thumbnail:
            self.generate_thumbnail()

    def generate_thumbnail(self):
        from PIL import Image as PILImage

        img = PILImage.open(self.image.path)
        img.thumbnail((200, 200))
        thumbnail_path = f'thumbnails/{self.image.name}'
        img.save(thumbnail_path)
        self.thumbnail = thumbnail_path
        self.save()

    def __str__(self):
        return self.image.name


class Plan(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username