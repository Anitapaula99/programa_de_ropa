from typing import List  # Importamos List para tipar las listas
import os  # Importamos os para limpiar la pantalla

# Clase base para todos los artículos de la tienda
class Articulo:
    def __init__(self, descripcion: str, costo: float, disponible: int, medida: str = ""):
        """
        Constructor de la clase Articulo
        Parámetros:
        - descripcion: nombre del artículo
        - costo: precio del artículo
        - disponible: cantidad en stock
        - medida: talla o medida del artículo
        """
        self._descripcion = descripcion
        self._costo = costo
        self._disponible = disponible
        self._medida = medida

    # Propiedades para acceder a los atributos privados
    @property
    def descripcion(self) -> str:
        return self._descripcion

    @property
    def costo(self) -> float:
        return self._costo

    @property
    def disponible(self) -> int:
        return self._disponible

    @property
    def medida(self) -> str:
        return self._medida

    def obtener_detalles(self) -> str:
        """Retorna una cadena formateada con los detalles del artículo"""
        return f"{self._descripcion:<20} | ${self._costo:>10,.0f} | Disp: {self._disponible:>3} | Med: {self._medida:<4}"

    def vender(self) -> None:
        """Reduce el stock del artículo en una unidad si hay disponibilidad"""
        if self._disponible > 0:
            self._disponible -= 1

# Clase para artículos de moda masculina
class ModaVarones(Articulo):
    def __init__(self, descripcion: str, costo: float, disponible: int, medida: str):
        """Hereda de Articulo y agrega el tipo 'Varones'"""
        super().__init__(descripcion, costo, disponible, medida)
        self._tipo = "Varones"

    def obtener_detalles(self) -> str:
        """Extiende el método de la clase base para incluir el tipo"""
        return f"{super().obtener_detalles()} | {self._tipo}"

# Clase para artículos de moda femenina
class ModaDamas(Articulo):
    def __init__(self, descripcion: str, costo: float, disponible: int, medida: str):
        """Hereda de Articulo y agrega el tipo 'Damas'"""
        super().__init__(descripcion, costo, disponible, medida)
        self._tipo = "Damas"

    def obtener_detalles(self) -> str:
        """Extiende el método de la clase base para incluir el tipo"""
        return f"{super().obtener_detalles()} | {self._tipo}"

# Clase para manejar las secciones de la tienda
class Seccion:
    def __init__(self, titulo: str):
        """
        Constructor de la sección
        - titulo: nombre de la sección
        - _articulos: lista para almacenar los artículos de la sección
        """
        self._titulo = titulo
        self._articulos: List[Articulo] = []

    @property
    def titulo(self) -> str:
        return self._titulo

    def agregar_articulo(self, articulo: Articulo) -> None:
        """Agrega un nuevo artículo a la sección"""
        self._articulos.append(articulo)

    def mostrar_catalogo(self) -> None:
        """Muestra todos los artículos de la sección en formato tabular"""
        if self._articulos:
            print(f"\n{self._titulo}:")
            print("-" * 70)
            print("Artículo             | Precio      | Disp | Med  | Tipo")
            print("-" * 70)
            for articulo in self._articulos:
                print(articulo.obtener_detalles())

# Clase principal que maneja toda la tienda
class Tienda:
    def __init__(self):
        """Inicializa la tienda con una lista vacía de secciones"""
        self._secciones: List[Seccion] = []

    def agregar_seccion(self, seccion: Seccion) -> None:
        """Agrega una nueva sección a la tienda"""
        self._secciones.append(seccion)

    def limpiar_consola(self) -> None:
        """Limpia la pantalla de la consola (compatible con Windows y Unix)"""
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_catalogo(self) -> None:
        """Muestra el catálogo completo de la tienda"""
        self.limpiar_consola()
        print("\n=== BOUTIQUE LANITA ===\n")
        for seccion in self._secciones:
            seccion.mostrar_catalogo()

    def realizar_venta(self, nombre_articulo: str, tipo: str) -> None:
        """
        Procesa la venta de un artículo
        - nombre_articulo: nombre del artículo a vender
        - tipo: 'Varones' o 'Damas'
        """
        for seccion in self._secciones:
            for articulo in seccion._articulos:
                # Verifica si el artículo existe y coincide el tipo
                if articulo.descripcion.lower() == nombre_articulo.lower() and (
                    (isinstance(articulo, ModaVarones) and tipo.lower() == "varones")
                    or (isinstance(articulo, ModaDamas) and tipo.lower() == "damas")
                ):
                    if articulo.disponible > 0:
                        articulo.vender()
                        print("\n" + "=" * 70)
                        print("Venta procesada exitosamente:")
                        print("-" * 70)
                        print(articulo.obtener_detalles())
                        print("=" * 70)
                        return
                    else:
                        print("\nArtículo agotado.")
                        return
        print("\nArtículo no encontrado.")

# Función principal que ejecuta el programa
def main():
    # Inicialización de la tienda
    tienda = Tienda()

    # Creación de las secciones principales
    seccion_superior = Seccion("PRENDAS SUPERIORES")
    seccion_inferior = Seccion("PRENDAS INFERIORES")
    seccion_zapatos = Seccion("CALZADOS")

    # Definición del catálogo para varones
    superiores_varones = [
        ModaVarones("Polo Ejecutivo", 89000, 8, "M"),
        ModaVarones("Remera Sport", 59000, 12, "L"),
        ModaVarones("Camiseta Gym", 49000, 15, "XL"),
    ]

    inferiores_varones = [
        ModaVarones("Jeans Classic", 99000, 10, "32"),
        ModaVarones("Pantalón Formal", 125000, 6, "34"),
        ModaVarones("Bermuda Sport", 69000, 14, "36"),
    ]

    calzados_varones = [
        ModaVarones("Mocasines Cuero", 155000, 8, "42"),
        ModaVarones("Tenis Deportivos", 185000, 12, "43"),
        ModaVarones("Ojotas Verano", 39000, 18, "41"),
    ]

    # Definición del catálogo para damas
    superiores_damas = [
        ModaDamas("Top Elegante", 79000, 10, "S"),
        ModaDamas("Remera Fashion", 65000, 15, "M"),
        ModaDamas("Musculosa Sport", 45000, 20, "L"),
    ]

    inferiores_damas = [
        ModaDamas("Jeans Fashion", 89000, 12, "28"),
        ModaDamas("Falda Ejecutiva", 115000, 8, "30"),
        ModaDamas("Calza Deportiva", 59000, 18, "32"),
    ]

    calzados_damas = [
        ModaDamas("Stilettos", 165000, 6, "37"),
        ModaDamas("Sneakers", 175000, 10, "38"),
        ModaDamas("Sandalias Verano", 49000, 15, "36"),
    ]

    # Agregar artículos a las secciones correspondientes
    for articulo in superiores_varones + superiores_damas:
        seccion_superior.agregar_articulo(articulo)

    for articulo in inferiores_varones + inferiores_damas:
        seccion_inferior.agregar_articulo(articulo)

    for articulo in calzados_varones + calzados_damas:
        seccion_zapatos.agregar_articulo(articulo)

    # Configurar la tienda con todas las secciones
    tienda.agregar_seccion(seccion_superior)
    tienda.agregar_seccion(seccion_inferior)
    tienda.agregar_seccion(seccion_zapatos)

    # Bucle principal del programa
    while True:
        tienda.mostrar_catalogo()
        print("\nMenú Principal:")
        print("=" * 70)
        print("1. Realizar venta")
        print("2. Finalizar programa")
        print("=" * 70)

        opcion = input("\nSeleccione una opción (1-2): ").strip()

        if opcion == "2":
            print("\n¡Gracias por utilizar el sistema!")
            print("=" * 70)
            break
        elif opcion == "1":
            articulo = input("Ingrese el nombre del artículo: ").strip()
            tipo = input("Ingrese el tipo (Varones/Damas): ").strip()
            tienda.realizar_venta(articulo, tipo)

            input("\nPresione Enter para volver al menú...")
        else:
            print("\nOpción inválida.")
            input("Presione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
