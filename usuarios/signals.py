from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def crear_superusuarios(sender, **kwargs):
    if sender.name != 'usuarios':
        return
    
    superusers = [
        ("andrea@gmail.com", "Andrea"),
        ("jorge@gmail.com", "Jorge"),
        ("juan@gmail.com", "Juan"),
    ]

    for email, nombre in superusers:
        if not User.objects.filter(email=email).exists():
            print(f"Creando superusuario {email}...")
            User.objects.create_superuser(
                email=email,
                nombre=nombre,
                password="123456"
            )

