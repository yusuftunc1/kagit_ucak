from django.contrib import admin
from .models import myuser
# Register your models here.


class myuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname','lastname','score')
    search_fields = ('username',)
    list_per_page = 20
    list_display_links = ('username',)


admin.site.register(myuser,myuserAdmin)