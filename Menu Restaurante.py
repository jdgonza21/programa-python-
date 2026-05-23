# Nombre estudiante: Jheyson Danilo Gonzalez Ocampo
# Grupo 213022_472
# Programa: Ingenieria de Sistemas 
# Codigo de fuente: Autoria propia

menu_restaurante = [
    ["Plato especial del dia", "Comida Criolla", 30000],
    ["Ensalada vegetal", "Saludable", 15000],
    ["Almuerzo ejecutivo", "Comida Criolla" , 25000],
    ["Bandeja Paisa", "Comida Criolla", 30000],
    ["Jugo Natural", "Bebidas", 8000],
    ["Gaseosa personal ", "Bebidas", 5000]
]

CATEGORIA_OBJETIVO = "Comida Criolla"
UMBRAL_PRECIO = 20000
DESCUENTO = 0.15

def calcular_precio_final(categoria, precio_base):

    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        descuento_aplicado = precio_base * DESCUENTO
        precio_final = precio_base - descuento_aplicado
    else:
        precio_final = precio_base

    return precio_final
print()
print("PRECIO FINAL DE LOS PRODUCTOS DEL MENÚ")

for producto in menu_restaurante:
    print("=" * 40)

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio Base: ${precio_base:,.0f}")
    print(f"Precio Final: ${precio_final:,.0f}")
    print()

print("¡Gracias por su compra!")
