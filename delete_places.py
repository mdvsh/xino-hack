import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xinohack.settings')

import django
django.setup()
from core.models import Places

def main():
    for i in Places.objects.all():
        i.delete()
        print(f"{i} has been deleted.")

if __name__ == '__main__':
    print("Initialized process of deleting places")
    main()