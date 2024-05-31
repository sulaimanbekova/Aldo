
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.name == 'products':  # Замените 'products' на имя вашего приложения
        categories = ['Акции', 'Завтраки', 'Кофе', 'Напитки', 'Чаи']
        for category in categories:
            Category.objects.get_or_create(name=category)
