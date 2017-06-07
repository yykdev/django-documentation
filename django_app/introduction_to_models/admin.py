from django.contrib import admin

# Register your models here.
# from django_app.introduction_to_models.models import Person
# from introduction_to_models.models import Person
from .models import Person

admin.site.register(Person)
