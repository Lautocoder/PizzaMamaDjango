from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredient', 'vegetarienne', 'prix')
    search_fields = ('nom', 'ingredient', 'vegetarienne', 'prix')

admin.site.register( Pizza, PizzaAdmin)
