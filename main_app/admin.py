from django.contrib import admin
from .models import Student, Class, Photo

# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Photo)