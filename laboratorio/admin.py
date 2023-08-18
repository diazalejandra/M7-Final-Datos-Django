from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    ordering = ("id", )

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "laboratorio")
    ordering = ("id", )

class ProductoAdmin(admin.ModelAdmin):  
    list_display = ("id", "nombre", "laboratorio", "get_year_fabricacion", "p_costo", "p_venta")
    list_filter = ("nombre", "laboratorio")
    ordering = ("id", )

    def get_year_fabricacion(self, obj):
        if obj.f_fabricacion is not None:
            return obj.f_fabricacion.year
    get_year_fabricacion.short_description = "F Fabricacion"


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)