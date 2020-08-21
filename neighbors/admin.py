from django.contrib import admin
from .models import neighbourhood,Business,User

# Register your models here.
class neighbourhoodAdmin(admin.ModelAdmin):
    list_display = ('name','location','count')
    list_display_links = ('name',)
    list_editable = ('count',)
    list_per_page = 10
    search_fields = ('name','location','count')
    list_filter = ('name','location')




admin.site.register(neighbourhood,neighbourhoodAdmin)
admin.site.register(Business)
admin.site.register(User)