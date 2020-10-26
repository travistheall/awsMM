from django.contrib import admin
from .models import (
    Profile,
    Weight,
    Meal,
    Food
)

admin.site.register(Weight),
admin.site.register(Meal),
admin.site.register(Profile),
admin.site.register(Food),
