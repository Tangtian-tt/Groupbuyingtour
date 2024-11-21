from django.contrib import admin
from .models import Abroad,Review

# Register your models here.
class AbroadAdmin(admin.ModelAdmin):
  list_display = ('title', 'description')
  search_fields = ['title', 'description']
  list_editable = ('description',)
admin.site.register(Abroad, AbroadAdmin)
admin.site.register(Review)
