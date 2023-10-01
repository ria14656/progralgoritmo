# Importamos el módulo json para trabajar con archivos de texto en formato JSON
import json

# Definimos una clase Tarea que representa una tarea con título, descripción y fecha de vencimiento
class Tarea:
    def _init_(self, titulo, descripcion, fecha=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
    
    def _str_(self):
        # Definimos un método para mostrar la información de la tarea de forma amigable
        if self.fecha:
            return f"{self.titulo} - {self.descripcion} - Vence el {self.fecha}"
        else:
            return f"{self.titulo} - {self.descripcion}"

# Definimos una función para cargar los datos de las tareas desde un archivo de texto
def cargar_datos(nombre_archivo):
    # Intentamos abrir el archivo en modo lectura
    try:
        with open(nombre_archivo, "r") as archivo:
            # Leemos el contenido del archivo y lo convertimos a una lista de diccionarios
            datos = json.load(archivo)
            # Creamos una lista vacía para almacenar las tareas
            tareas = []
            # Recorremos la lista de diccionarios y creamos objetos Tarea con los datos
            for dato in datos:
                tarea = Tarea(dato["titulo"], dato["descripcion"], dato["fecha"])
                # Agregamos la tarea a la lista de tareas
                tareas.append(tarea)
            # Retornamos la lista de tareas
            return tareas
    # Si ocurre algún error al abrir el archivo, retornamos una lista vacía
    except:
        return []

# Definimos una función para guardar los datos de las tareas en un archivo de texto
def guardar_datos(nombre_archivo, tareas):
    # Intentamos abrir el archivo en modo escritura
    try:
        with open(nombre_archivo, "w") as archivo:
            # Creamos una lista vacía para almacenar los datos de las tareas en formato diccionario
            datos = []
            # Recorremos la lista de tareas y extraemos sus atributos
            for tarea in tareas:
                dato = {"titulo": tarea.titulo, "descripcion": tarea.descripcion, "fecha": tarea.fecha}
                # Agregamos el dato a la lista de datos
                datos.append(dato)
            # Convertimos la lista de datos a un formato JSON y lo escribimos en el archivo
            json.dump(datos, archivo)
    # Si ocurre algún error al abrir el archivo, mostramos un mensaje de error
    except:
        print("No se pudo guardar los datos en el archivo.")

# Definimos una función para agregar una nueva tarea a la lista de tareas pendientes
def agregar_tarea(tareas_pendientes):
    # Pedimos al usuario que ingrese el título y la descripción de la tarea
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    # Opcional: Pedimos al usuario que ingrese la fecha de vencimiento de la tarea
    fecha = input("Ingrese la fecha de vencimiento de la tarea (opcional): ")
    # Creamos un objeto Tarea con los datos ingresados por el usuario
    tarea = Tarea(titulo, descripcion, fecha)
    # Agregamos la tarea a la lista de tareas pendientes
    tareas_pendientes.append(tarea)
    # Mostramos un mensaje de confirmación
    print("Se ha agregado la tarea a la lista de tareas pendientes.")

# Definimos una función para listar las tareas pendientes o completadas según el parámetro recibido
def listar_tareas(tareas):
    # Verificamos si la lista de tareas está vacía o no
    if tareas:
        # Si no está vacía, recorremos la lista y mostramos cada tarea con su índice
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")
    else:
        # Si está vacía, mostramos un mensaje indicando que no hay tareas
        print("No hay tareas en esta lista.")

# Definimos una función para marcar una tarea como completada y moverla a la lista de tareas completadas
def marcar_tarea(tareas_pendientes, tareas_completadas):
    # Verificamos si la lista de tareas pendientes está vacía o no
    if tareas_pendientes:
        # Si no está vacía, pedimos al usuario que ingrese el índice de la tarea que quiere marcar como completada
        indice = int(input("Ingrese el número de la tarea que quiere marcar como completada: ")) - 1
        # Verificamos si el índice es válido o no
        if 0 <= indice < len(tareas_pendientes):
            # Si es válido, obtenemos la tarea correspondiente al índice
            tarea = tareas_pendientes[indice]
            # Eliminamos la tarea de la lista de tareas pendientes
            tareas_pendientes.pop(indice)
            # Agregamos la tarea a la lista de tareas completadas
            tareas_completadas.append(tarea)
            # Mostramos un mensaje de confirmación
            print("Se ha marcado la tarea como completada y se ha movido a la lista de tareas completadas.")
        else:
            # Si no es válido, mostramos un mensaje de error
            print("El número ingresado no corresponde a ninguna tarea.")
    else:
        # Si está vacía, mostramos un mensaje indicando que no hay tareas pendientes
        print("No hay tareas pendientes que marcar como completadas.")

# Definimos una función para mostrar las opciones del menú y pedir al usuario que elija una
def mostrar_menu():
    # Mostramos las opciones del menú
    print("Menú de opciones:")
    print("1. Agregar una tarea")
    print("2. Listar tareas pendientes")
    print("3. Listar tareas completadas")
    print("4. Marcar tarea como completada")
    print("5. Salir")
    # Pedimos al usuario que ingrese el número de la opción que quiere elegir
    opcion = int(input("Ingrese el número de la opción que quiere elegir: "))
    # Retornamos la opción elegida por el usuario
    return opcion

# Definimos los nombres de los archivos donde se guardarán los datos de las tareas pendientes y completadas
archivo_pendientes = "tareas_pendientes.json"
archivo_completadas = "tareas_completadas.json"

# Cargamos los datos de las tareas pendientes y completadas desde los archivos de texto
tareas_pendientes = cargar_datos(archivo_pendientes)
tareas_completadas = cargar_datos(archivo_completadas)

# Mostramos un mensaje de bienvenida al programa
print("Bienvenido al programa para llevar un registro de sus tareas.")

# Creamos una variable para controlar el bucle del menú
continuar = True

# Mientras el usuario quiera continuar con el programa, repetimos el bucle del menú
while continuar:
    # Mostramos el menú y obtenemos la opción elegida por el usuario
    opcion = mostrar_menu()
    # Verificamos qué opción eligió el usuario y ejecutamos la función correspondiente
    if opcion == 1:
        # Si eligió la opción 1, llamamos a la función para agregar una nueva tarea
        agregar_tarea(tareas_pendientes)
    elif opcion == 2:
        # Si eligió la opción 2, llamamos a la función para listar las tareas pendientes
        listar_tareas(tareas_pendientes)
    elif opcion == 3:
        # Si eligió la opción 3, llamamos a la función para listar las tareas completadas
        listar_tareas(tareas_completadas)
    elif opcion == 4:
        # Si eligió la opción 4, llamamos a la función para marcar una tarea como completada
        marcar_tarea(tareas_pendientes, tareas_completadas)
    elif opcion == 5:
        # Si eligió la opción 5, salimos del bucle del menú y terminamos el programa
        continuar = False
    else:
        # Si eligió una opción inválida, mostramos un mensaje de error
        print("La opción ingresada no es válida. Por favor, ingrese un número entre 1 y 5.")

# Antes de terminar el programa, guardamos los datos de las tareas pendientes y completadas en los archivos de texto
guardar_datos(archivo_pendientes, tareas_pendientes)
guardar_datos(archivo_completadas, tareas_completadas)

# Mostramos un mensaje de despedida al usuario
print("Gracias nuestro programa. Hasta pronto.")
