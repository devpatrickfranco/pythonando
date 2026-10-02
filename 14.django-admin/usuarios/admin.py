from django.contrib import admin

from .models import Clientes, Sintomas, ClienteSintoma


class ClienteSintomaInline(admin.TabularInline):
    model = ClienteSintoma
    extra = 0


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'queixa', 'get_foto')
    search_fields = ('nome', 'email', 'id')
    list_filter = ('queixa',)
    list_editable = ('queixa',)

    inlines = [ClienteSintomaInline]


@admin.register(Sintomas)
class SintomasAdmin(admin.ModelAdmin):
    inlines = [ClienteSintomaInline]