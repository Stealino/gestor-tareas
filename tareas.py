"""Gestor de tareas por consola.

Guarda las tareas en un archivo JSON (tareas.json) para que no se pierdan
al cerrar el programa. No requiere librerías externas.
"""
import json
import os

ARCHIVO = "tareas.json"


def cargar():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)


def listar(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.")
        return
    print("\n--- Tus tareas ---")
    for i, t in enumerate(tareas, start=1):
        estado = "✔" if t["hecha"] else " "
        print(f"{i}. [{estado}] {t['titulo']}")


def agregar(tareas):
    titulo = input("Título de la nueva tarea: ").strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return
    tareas.append({"titulo": titulo, "hecha": False})
    guardar(tareas)
    print("Tarea agregada.")


def pedir_numero(tareas):
    try:
        n = int(input("Número de la tarea: "))
    except ValueError:
        print("Debes escribir un número.")
        return None
    if not 1 <= n <= len(tareas):
        print("Ese número no existe.")
        return None
    return n - 1


def completar(tareas):
    listar(tareas)
    idx = pedir_numero(tareas) if tareas else None
    if idx is not None:
        tareas[idx]["hecha"] = True
        guardar(tareas)
        print("Tarea marcada como completada.")


def eliminar(tareas):
    listar(tareas)
    idx = pedir_numero(tareas) if tareas else None
    if idx is not None:
        quitada = tareas.pop(idx)
        guardar(tareas)
        print(f"Tarea eliminada: {quitada['titulo']}")


def menu():
    tareas = cargar()
    opciones = {
        "1": ("Ver tareas", listar),
        "2": ("Agregar tarea", agregar),
        "3": ("Completar tarea", completar),
        "4": ("Eliminar tarea", eliminar),
    }
    while True:
        print("\n=== GESTOR DE TAREAS ===")
        for clave, (texto, _) in opciones.items():
            print(f"{clave}. {texto}")
        print("5. Salir")
        eleccion = input("Elige una opción: ").strip()
        if eleccion == "5":
            print("¡Hasta pronto!")
            break
        if eleccion in opciones:
            opciones[eleccion][1](tareas)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
