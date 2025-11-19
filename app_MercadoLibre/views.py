from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendedor
# app_MercadoLibre/views.py (añadir estas funciones)
from .models import Categoria
from .models import Producto
from .models import Usuario
from .models import Calificacion
from .models import Transaccion
from .models import Pedido

# ================================
# CRUD PEDIDO
# ================================


def agregar_pedido(request):
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()
    vendedores = Vendedor.objects.all()
    transacciones = Transaccion.objects.all()
    if request.method == 'POST':
        Pedido.objects.create(
            usuario_id=request.POST['usuario'],
            producto_id=request.POST['producto'],
            vendedor_id=request.POST['vendedor'],
            id_transaccion_id=request.POST['id_transaccion'],
            total=request.POST['total'],
            estado=request.POST['estado'],
            direccion_envio=request.POST['direccion_envio'],
            pais_envio=request.POST['pais_envio'],
        )
        return redirect('ver_pedido')
    return render(request, 'pedido/agregar_pedido.html', {
        'usuarios': usuarios, 'productos': productos,
        'vendedores': vendedores, 'transacciones': transacciones
    })

def ver_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/ver_pedido.html', {'pedidos': pedidos})

def actualizar_pedido(request, id_pedido):
    pedido = Pedido.objects.get(id_pedido=id_pedido)
    usuarios = Usuario.objects.all()
    productos = Producto.objects.all()
    vendedores = Vendedor.objects.all()
    transacciones = Transaccion.objects.all()

    if request.method == "POST":
        pedido.usuario_id = request.POST.get("usuario")
        pedido.producto_id = request.POST.get("producto")
        pedido.vendedor_id = request.POST.get("vendedor")
        pedido.id_transaccion_id = request.POST.get("id_transaccion")


        pedido.total = request.POST.get("total")
        pedido.estado = request.POST.get("estado")
        pedido.direccion_envio = request.POST.get("direccion_envio")
        pedido.pais_envio = request.POST.get("pais_envio")

        # OJO: NO cambies fecha_pedido si es auto_now_add
        # pedido.fecha_pedido = request.POST.get("fecha_pedido")

        pedido.save()
        return redirect("ver_pedido")

    return render(request, "pedido/actualizar_pedido.html", {
        "pedido": pedido,
        "usuarios": usuarios,
        "productos": productos,
        "vendedores": vendedores,
        "transacciones": transacciones,
    })



def borrar_pedido(request, id):
    pedido = Pedido.objects.get(id_pedido=id)

    if request.method == "POST":
        pedido.delete()
        return redirect('ver_pedido')

    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})


# ================================
# CRUD TRANSACCION
# ================================

def agregar_transaccion(request):
    usuarios = Usuario.objects.all()
    vendedores = Vendedor.objects.all()
    if request.method == 'POST':
        Transaccion.objects.create(
            usuario_id=request.POST['usuario'],
            banco_usuario=request.POST['banco_usuario'],
            vendedor_id=request.POST['vendedor'],
            banco_vendedor=request.POST['banco_vendedor'],
            monto_total=request.POST['monto_total'],
            tipo=request.POST['tipo'],
            estado=request.POST['estado'],
        )
        return redirect('ver_transaccion')
    return render(request, 'transaccion/agregar_transaccion.html', {
        'usuarios': usuarios, 'vendedores': vendedores
    })

def ver_transaccion(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'transaccion/ver_transaccion.html', {'transacciones': transacciones})

def actualizar_transaccion(request, id):
    transaccion = Transaccion.objects.get(id_transaccion=id)
    usuarios = Usuario.objects.all()
    vendedores = Vendedor.objects.all()
    if request.method == 'POST':
        transaccion.usuario_id = request.POST['usuario']
        transaccion.vendedor_id = request.POST['vendedor']
        transaccion.banco_usuario = request.POST['banco_usuario']
        transaccion.banco_vendedor = request.POST['banco_vendedor']
        transaccion.monto_total = request.POST['monto_total']
        transaccion.tipo = request.POST['tipo']
        transaccion.estado = request.POST['estado']
        transaccion.save()
        return redirect('ver_transaccion')
    return render(request, 'transaccion/actualizar_transaccion.html', {
        'transaccion': transaccion,
        'usuarios': usuarios,
        'vendedores': vendedores
    })

def borrar_transaccion(request, id):
    transaccion = Transaccion.objects.get(id_transaccion=id)

    if request.method == "POST":
        transaccion.delete()
        return redirect('ver_transaccion')

    return render(request, 'transaccion/borrar_transaccion.html', {'transaccion': transaccion})



# ================================
# CRUD CALIFICACION
# ================================

def agregar_calificacion(request):
    productos = Producto.objects.all()
    vendedores = Vendedor.objects.all()
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        Calificacion.objects.create(
            producto_id=request.POST['producto'],
            vendedor_id=request.POST['vendedor'],
            usuario_id=request.POST['usuario'],
            puntuacion=request.POST['puntuacion'],
            comentario=request.POST['comentario'],
        )
        return redirect('ver_calificacion')
    return render(request, 'calificacion/agregar_calificacion.html', {
        'productos': productos, 'vendedores': vendedores, 'usuarios': usuarios
    })

def ver_calificacion(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'calificacion/ver_calificacion.html', {'calificaciones': calificaciones})

def actualizar_calificacion(request, id):
    calificacion = Calificacion.objects.get(id_calificacion=id)
    productos = Producto.objects.all()
    vendedores = Vendedor.objects.all()
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        calificacion.producto_id = request.POST['producto']
        calificacion.vendedor_id = request.POST['vendedor']
        calificacion.usuario_id = request.POST['usuario']
        calificacion.puntuacion = request.POST['puntuacion']
        calificacion.comentario = request.POST['comentario']
        calificacion.save()
        return redirect('ver_calificacion')
    return render(request, 'calificacion/actualizar_calificacion.html', {
        'calificacion': calificacion,
        'productos': productos,
        'vendedores': vendedores,
        'usuarios': usuarios
    })

def borrar_calificacion(request, id):
    calificacion = Calificacion.objects.get(id_calificacion=id)

    if request.method == "POST":
        calificacion.delete()
        return redirect('ver_calificacion')

    return render(request, 'calificacion/borrar_calificacion.html', {'calificacion': calificacion})



# ================================
# CRUD USUARIO
# ================================
def agregar_usuario(request):
    if request.method == 'POST':
        Usuario.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            email=request.POST['email'],
            password=request.POST['password'],
            direccion=request.POST['direccion'],
            ciudad=request.POST['ciudad'],
            pais=request.POST['pais'],
            telefono=request.POST['telefono'],
        )
        return redirect('ver_usuario')
    return render(request, 'usuario/agregar_usuario.html')

def ver_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/ver_usuario.html', {'usuarios': usuarios})

def actualizar_usuario(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.email = request.POST['email']
        usuario.direccion = request.POST['direccion']
        usuario.ciudad = request.POST['ciudad']
        usuario.pais = request.POST['pais']
        usuario.telefono = request.POST['telefono']
        usuario.save()
        return redirect('ver_usuario')
    return render(request, 'usuario/actualizar_usuario.html', {'usuario': usuario})

def borrar_usuario(request, id):
    usuario = Usuario.objects.get(id_usuario=id)

    if request.method == "POST":
        usuario.delete()
        return redirect('ver_usuario')

    return render(request, 'usuario/borrar_usuario.html', {'usuario': usuario})


def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        precio = request.POST.get("precio", 0)
        stock = request.POST.get("stock", 0)
        descripcion = request.POST.get("descripcion", "")
        disponible = True if request.POST.get("disponible") == "on" else False

        # FK vendedor (select)
        id_vendedor = request.POST.get("vendedor")
        vendedor = Vendedor.objects.get(id_vendedor=id_vendedor) if id_vendedor else None

        producto = Producto.objects.create(
            nombre=nombre,
            precio=int(precio) if precio else 0,
            stock=int(stock) if stock else 0,
            descripcion=descripcion,
            disponible=disponible,
            vendedor=vendedor
        )

        # categorias (many-to-many) — puede venir como lista o un solo valor
        categorias_ids = request.POST.getlist("categorias")
        if categorias_ids:
            producto.categorias.set(categorias_ids)

        return redirect("ver_producto")

    vendedores = Vendedor.objects.all().order_by("nombre")
    categorias = Categoria.objects.filter(activa=True).order_by("nombre")
    return render(request, "producto/agregar_producto.html", {"vendedores": vendedores, "categorias": categorias})


# Ver productos (tabla)
def ver_producto(request):
    productos = Producto.objects.all().order_by("-fecha_publicacion")
    return render(request, "producto/ver_producto.html", {"productos": productos})


# Mostrar formulario para actualizar producto
def actualizar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    vendedores = Vendedor.objects.all().order_by("nombre")
    categorias = Categoria.objects.filter(activa=True).order_by("nombre")
    return render(request, "producto/actualizar_producto.html", {
        "producto": producto,
        "vendedores": vendedores,
        "categorias": categorias
    })


# Realizar actualización (POST)
def realizar_actualizacion_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == "POST":
        producto.nombre = request.POST.get("nombre", producto.nombre)
        producto.precio = int(request.POST.get("precio", producto.precio) or producto.precio)
        producto.stock = int(request.POST.get("stock", producto.stock) or producto.stock)
        producto.descripcion = request.POST.get("descripcion", producto.descripcion)
        producto.disponible = True if request.POST.get("disponible") == "on" else False

        id_vendedor = request.POST.get("vendedor")
        if id_vendedor:
            producto.vendedor = Vendedor.objects.get(id_vendedor=id_vendedor)

        producto.save()

        categorias_ids = request.POST.getlist("categorias")
        if categorias_ids:
            producto.categorias.set(categorias_ids)
        else:
            producto.categorias.clear()

        return redirect("ver_producto")
    return redirect("actualizar_producto", id_producto=id_producto)


# Borrar — confirmar y eliminar
def borrar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == "POST":
        producto.delete()
        return redirect("ver_producto")
    return render(request, "producto/borrar_producto.html", {"producto": producto})
# Agregar categoria (form simple POST)
def agregar_categoria(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        descripcion = request.POST.get("descripcion", "")
        tipo = request.POST.get("tipo", "")
        img_url = request.POST.get("img_url", "")
        activa = True if request.POST.get("activa") == "on" else False

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            tipo=tipo,
            img_url=img_url,
            activa=activa
        )
        return redirect("ver_categoria")
    return render(request, "categoria/agregar_categoria.html")

# Ver categorias (lista en tabla)
def ver_categoria(request):
    categorias = Categoria.objects.all().order_by("-fecha_creacion")
    return render(request, "categoria/ver_categoria.html", {"categorias": categorias})

# Mostrar formulario para actualizar
def actualizar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    return render(request, "categoria/actualizar_categoria.html", {"categoria": categoria})

# Realizar actualización (POST)
def realizar_actualizacion_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == "POST":
        categoria.nombre = request.POST.get("nombre", categoria.nombre)
        categoria.descripcion = request.POST.get("descripcion", categoria.descripcion)
        categoria.tipo = request.POST.get("tipo", categoria.tipo)
        categoria.img_url = request.POST.get("img_url", categoria.img_url)
        categoria.activa = True if request.POST.get("activa") == "on" else False
        categoria.save()
        return redirect("ver_categoria")
    return redirect("actualizar_categoria", id_categoria=id_categoria)

# Borrar — confirmar y eliminar
def borrar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == "POST":
        categoria.delete()
        return redirect("ver_categoria")
    return render(request, "categoria/borrar_categoria.html", {"categoria": categoria})


# Página de inicio del sistema
def inicio_mercadolibre(request):
    contexto = {}
    return render(request, "inicio.html", contexto)

# Agregar vendedor (form simple POST)
def agregar_vendedor(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "")
        apellido = request.POST.get("apellido", "")
        email = request.POST.get("email", "")
        telefono = request.POST.get("telefono", "")
        direccion = request.POST.get("direccion", "")
        ciudad = request.POST.get("ciudad", "")
        # No validamos (según tu pedido)
        Vendedor.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion,
            ciudad=ciudad
        )
        return redirect("ver_vendedor")
    return render(request, "vendedor/agregar_vendedor.html")

# Ver vendedores (lista en tabla)
def ver_vendedor(request):
    vendedores = Vendedor.objects.all().order_by("-fecha_registro")
    return render(request, "vendedor/ver_vendedor.html", {"vendedores": vendedores})

# Actualizar — muestra formulario con datos
def actualizar_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    return render(request, "vendedor/actualizar_vendedor.html", {"vendedor": vendedor})

# Realizar actualización (POST)
def realizar_actualizacion_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    if request.method == "POST":
        vendedor.nombre = request.POST.get("nombre", vendedor.nombre)
        vendedor.apellido = request.POST.get("apellido", vendedor.apellido)
        vendedor.email = request.POST.get("email", vendedor.email)
        vendedor.telefono = request.POST.get("telefono", vendedor.telefono)
        vendedor.direccion = request.POST.get("direccion", vendedor.direccion)
        vendedor.ciudad = request.POST.get("ciudad", vendedor.ciudad)
        vendedor.save()
        return redirect("ver_vendedor")
    return redirect("actualizar_vendedor", id_vendedor=id_vendedor)

# Borrar — confirmar y eliminar
def borrar_vendedor(request, id_vendedor):
    vendedor = get_object_or_404(Vendedor, id_vendedor=id_vendedor)
    if request.method == "POST":
        vendedor.delete()
        return redirect("ver_vendedor")
    return render(request, "vendedor/borrar_vendedor.html", {"vendedor": vendedor})