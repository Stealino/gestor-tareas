# Gestor de Tareas por Consola

Aplicación sencilla en **Python** para administrar una lista de tareas desde la terminal. Las tareas se guardan en un archivo `tareas.json`, así que no se pierden al cerrar el programa.

## ¿Qué hace?

- Ver la lista de tareas (✔ indica que está completada)
- Agregar tareas nuevas
- Marcar tareas como completadas
- Eliminar tareas

## Requisitos

- Python 3.8 o superior (no necesita instalar librerías adicionales)

## Cómo ejecutarla

```bash
git clone https://github.com/Stealino/gestor-tareas.git
cd gestor-tareas
python tareas.py
```

## Cómo se usa

Al ejecutar el programa aparece un menú:

```
=== GESTOR DE TAREAS ===
1. Ver tareas
2. Agregar tarea
3. Completar tarea
4. Eliminar tarea
5. Salir
```

Escribe el número de la opción y presiona Enter. Para completar o eliminar una tarea, se muestra la lista y debes escribir el número de la tarea.

## Estructura del proyecto

```
gestor-tareas/
├── tareas.py     # Código de la aplicación
├── README.md     # Este archivo
└── .gitignore    # Archivos que Git debe ignorar
```

## Autor

Proyecto realizado por Jonathan Osorio para el taller de repositorios. Desarrollado con apoyo de IA.
