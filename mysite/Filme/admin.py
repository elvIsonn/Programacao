from django.contrib import admin

from .models import filmes, Generos

class GenerosAdmin(admin.ModelAdmin):
    list_display = ['genero']

class filmesAdmin(admin.ModelAdmin):
    list_display = ['filme', 'genero', 'quantidade', 'preco']
    ordering = ['-filme']
    search_fields = ['genero']
    list_filter = ['genero']
    list_editable = ['genero', 'quantidade', 'preco']

admin.site.register(filmes, filmesAdmin)
admin.site.register(Generos)

# Register your models here.
