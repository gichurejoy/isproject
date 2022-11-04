from django.contrib import admin

# Register your models here.
from .models import learner,instructor

admin.site.register(learner)
admin.site.register(instructor)