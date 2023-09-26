from django.db import models
from django.contrib.auth.models import User


class AccountTier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_sizes = models.CharField(max_length=255)
    show_original_link = models.BooleanField(default=False)
    generate_expiring_link = models.BooleanField(default=False)
    link_expiration_time = models.PositiveIntegerField(default=300, help_text='Link expiration time in seconds (300 - 30000)')

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    account_tier = models.ForeignKey(AccountTier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.image.name
