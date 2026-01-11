#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Try to configure Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
    django.setup()
    
    print("SUCCESS: Django setup worked!")
    print(f"DEBUG = {settings.DEBUG}")
    print(f"ALLOWED_HOSTS = {settings.ALLOWED_HOSTS}")
    print(f"DATABASES engine = {settings.DATABASES['default']['ENGINE']}")
    
    # Test database connection
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        print("SUCCESS: Database connection works!")
        
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
