# Generated by Django 4.2.5 on 2023-09-26 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thumbnail_sizes', models.CharField(max_length=255)),
                ('show_original_link', models.BooleanField(default=False)),
                ('generate_expiring_link', models.BooleanField(default=False)),
                ('link_expiration_time', models.PositiveIntegerField(default=300, help_text='Link expiration time in seconds (300 - 30000)')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account_tier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='images_api.accounttier')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
