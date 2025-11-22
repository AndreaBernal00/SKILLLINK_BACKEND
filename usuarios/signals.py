from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os

User = get_user_model()

SUPERUSERS = [
    {"email": "andrea@gmail.com", "nombre": "Andrea", "password": "admin123"},
    {"email": "jorge@gmail.com", "nombre": "Jorge", "password": "admin123"},
    {"email": "juan@gmail.com", "nombre": "Juan", "password": "admin123"},
]

@receiver(post_migrate)
def create_superusers(sender, **kwargs):
    if not os.environ.get("RENDER"):
        return

    for data in SUPERUSERS:
        if not User.objects.filter(email=data["email"]).exists():
            User.objects.create_superuser(
                email=data["email"],
                nombre=data["nombre"],
                password=data["password"]
            )
            print(f"Superusuario creado: {data['email']}")
        else:
            print(f"Superusuario ya existe: {data['email']}")
