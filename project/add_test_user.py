import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app1.models import User

test_user, created = User.objects.get_or_create(
    username='quantic',
    defaults={'password': 'pass123'}
)

if created:
    print("Test user 'quantic' created successfully!")
else:
    print("Test user 'quantic' already exists!")