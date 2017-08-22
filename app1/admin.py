from django.contrib import admin

from .models import MyQuestion, MyChoice

admin.site.register(MyQuestion)

admin.site.register(MyChoice)


# Register your models here.
