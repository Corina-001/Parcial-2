class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Perecedero(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        super().__init__(self, self.nombre, self.precio, self.cantidad)
        self.fecha_vencimiento = fecha_vencimiento
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

productos = []
productos.append(Producto("Crema de pastacho", 2,99, 7, "fecha_vencimiento"))
for producto in productos:
    if isinstance(producto, Perecedero):
        print(f'Producto, {producto.nombre}, Precio, {producto.precio}, Cantidad, {producto.cantidad}, se vence el {producto.fecha_vencimiento}')

fecha_vencimiento = input("Ingrese la fecha de vencimiento (DD/MM/AAAA): ")
print(f'El producto se vence el {fecha_vencimiento}')

class NoPerecedero(Producto):
    def __init__(self, nombre, precio, cantidad, material):
        super().__init__(self, self.nombre, self.precio, self.cantidad)
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.material = material

class Inventario:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)

ingresar_producto = input("Ingrese el nombre del producto")
ingresar_precio = input("Ingrese el precio del producto")
ingresar_cantidad = ("Ingresar la cantidad que hay del producto")
ingresar_material =("Ingresar el material del producto")
ingresar_fecha_vencimiento = ("Ingresar la fecha de vencimiento del producto (DD/MM/AAAA):  ")

print("Hay disponible: Producto, {self.productos}, Precio, {ingresar_precio}, Fecha de vencimiento, {fecha_vencimiento} ")
for producto in productos:
    if len(productos=ingresar_producto):
        print(f'El producto {ingresar_producto} ha sido eliminado')
    
    def
        total = {ingresar_precio + ingresar_cantidad}

    valor_total()