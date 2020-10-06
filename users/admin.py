from django.contrib import admin
from .models import (Profile,
                     Weight,
                     Photo,
                     Food)

admin.site.register(Weight),
admin.site.register(Photo),
admin.site.register(Profile),
admin.site.register(Food),

