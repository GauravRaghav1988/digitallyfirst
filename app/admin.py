from django.contrib import admin

from app.models import Client


# Register your models here.





@admin.register(Client)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email','password','created')


