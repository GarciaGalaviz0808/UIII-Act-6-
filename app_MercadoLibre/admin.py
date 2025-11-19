from django.contrib import admin
from .models import Vendedor, Categoria, Producto, Usuario, Calificacion, Transaccion, Pedido

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ("id_vendedor", "nombre", "apellido", "email", "telefono", "ciudad", "fecha_registro")
    search_fields = ("nombre", "apellido", "email", "ciudad")


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre", "tipo", "activa", "fecha_creacion")
    search_fields = ("nombre", "tipo")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id_producto", "nombre", "vendedor", "precio", "stock", "disponible", "fecha_publicacion")
    list_filter = ("disponible", "vendedor")
    search_fields = ("nombre", "descripcion")

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id_usuario",
        "nombre",
        "apellido",
        "email",
        "password",
        "fecha_registro",
        "direccion",
        "ciudad",
        "pais",
        "telefono",
    )
    search_fields = ("nombre", "apellido", "email", "pais", "ciudad")
    list_filter = ("pais", "ciudad")
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("id_calificacion", "producto", "vendedor", "usuario", "puntuacion", "fecha")
    list_filter = ("puntuacion",)
    search_fields = ("comentario",)

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ("id_transaccion", "usuario", "vendedor", "tipo", "estado", "monto_total", "fecha")
    list_filter = ("tipo", "estado")
    search_fields = ("usuario__nombre", "vendedor__nombre")

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id_pedido", "usuario", "producto", "vendedor", "total", "estado", "fecha_pedido")
    list_filter = ("estado",)
    search_fields = ("usuario__nombre", "producto__nombre")