from django.contrib import admin
from .models import Tour,Review

# Register your models here.
class TourAdmin(admin.ModelAdmin):
  list_display = ('title', 'description')
  search_fields = ['title', 'description']
  list_editable = ('description',)
admin.site.register(Tour, TourAdmin)
admin.site.register(Review)
