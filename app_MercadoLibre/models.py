from django.db import models

# ==========================================
# MODELO: VENDEDOR
# ==========================================
class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=300, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=300)
    ciudad = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: CATEGORIA (pendiente)
# ==========================================
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    img_url = models.URLField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: PRODUCTO (pendiente)
# ==========================================
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, unique=True)

    vendedor = models.ForeignKey(
        Vendedor, on_delete=models.CASCADE, related_name="productos"
    )

    categorias = models.ManyToManyField(
        Categoria, related_name="productos"
    )

    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=200)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: USUARIO
# ==========================================
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    direccion = models.CharField(max_length=400)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: CALIFICACION
# ==========================================
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True, unique=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"⭐ {self.puntuacion} - {self.usuario}"


# ==========================================
# MODELO: TRANSACCION
# ==========================================
class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('pago', 'Pago'),
        ('reembolso', 'Reembolso'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]

    id_transaccion = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    banco_usuario = models.CharField(max_length=200)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    banco_vendedor = models.CharField(max_length=200)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Transacción {self.id_transaccion} - {self.tipo}"


# ==========================================
# MODELO: PEDIDO
# ==========================================
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]

    id_pedido = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    direccion_envio = models.CharField(max_length=400)
    pais_envio = models.CharField(max_length=100)



    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.estado}"