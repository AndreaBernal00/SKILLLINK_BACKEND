from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

superusers = [
    {"email": "andrea@gmail.com", "nombre": "Andrea", "password": "admin123"},
    {"email": "jorge@gmail.com", "nombre": "Jorge", "password": "admin123"},
    {"email": "juan@gmail.com", "nombre": "Juan", "password": "admin123"},
]

def create_superusers():
    for data in superusers:
        try:
            if not User.objects.filter(email=data["email"]).exists():
                User.objects.create_superuser(
                    email=data["email"],
                    nombre=data["nombre"],
                    password=data["password"]
                )
                print(f"Superusuario creado: {data['email']}")
            else:
                print(f"Superusuario ya existe: {data['email']}")
        except IntegrityError:
            print(f"Error creando superusuario: {data['email']} (ya existe)")
