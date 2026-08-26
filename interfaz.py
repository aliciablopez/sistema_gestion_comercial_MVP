# ==============================================================================
# INTERFAZ DE LA APLICACIÓN
# ==============================================================================

# tkinter contiene los elementos básicos de la interfaz gráfica.

import tkinter as tk


# ttk contiene widgets adicionales de Tkinter.
#
# En este ejercicio utilizamos:
#
#   - Notebook → organiza las pestañas
#   - Frame    → sirve como contenedor de cada pestaña

from tkinter import ttk


# ==============================================================================
# IMPORTACIÓN DE LOS MÓDULOS DEL SISTEMA
# ==============================================================================

# CAMBIO IMPORTANTE
# ------------------------------------------------------------------------------
#
# Antes interfaz.py solamente creaba las pestañas y colocaba un texto
# provisional dentro de cada una.
#
# Ahora interfaz.py debe llamar a cada módulo para que ese módulo
# construya el contenido de su propia pestaña.
#
# Por eso importamos las cinco clases.

from clientes import Clientes
from empleados import Empleados
from proveedores import Proveedores
from stock import Stock
from facturacion import Facturacion


# ==============================================================================
# FUNCIÓN PRINCIPAL DE LA INTERFAZ
# ==============================================================================

def iniciar_aplicacion():

    # --------------------------------------------------------------------------
    # 1. CREAR LA VENTANA PRINCIPAL
    # --------------------------------------------------------------------------

    # tk.Tk() crea la ventana raíz de la aplicación.
    #
    # Esta es la ÚNICA ventana principal del programa.

    ventana = tk.Tk()


    ventana.title(
        "Sistema de Gestión Comercial"
    )


    ventana.geometry(
        "900x600"
    )


    # Evitamos que el usuario cambie el tamaño de la ventana.

    ventana.resizable(
        False,
        False
    )


    # --------------------------------------------------------------------------
    # 2. CREAR EL NOTEBOOK
    # --------------------------------------------------------------------------

    # Notebook es un widget de ttk que permite organizar
    # diferentes contenidos mediante pestañas.
    #
    # El Notebook pertenece a la ventana principal.

    notebook = ttk.Notebook(
        ventana
    )


    # Colocamos el Notebook dentro de la ventana principal.
    #
    # pack() se utiliza aquí porque estamos colocando el Notebook
    # como una zona general dentro de la ventana.
    #
    # fill="both" → ocupa horizontal y verticalmente el espacio disponible.
    #
    # expand=True → permite que se expanda cuando la ventana dispone
    # de espacio adicional.

    notebook.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )


    # --------------------------------------------------------------------------
    # 3. CREAR LAS PESTAÑAS
    # --------------------------------------------------------------------------

    # Cada pestaña será un Frame.
    #
    # Un Frame es un widget contenedor:
    # permite colocar dentro otros widgets.
    #
    # IMPORTANTE:
    #
    # interfaz.py CREA las pestañas.
    #
    # Los módulos NO las crean.
    #
    # Esta es la decisión arquitectónica que estamos utilizando
    # en todo el laboratorio.


    pestana_clientes = ttk.Frame(
        notebook
    )


    pestana_empleados = ttk.Frame(
        notebook
    )


    pestana_proveedores = ttk.Frame(
        notebook
    )


    pestana_stock = ttk.Frame(
        notebook
    )


    pestana_facturacion = ttk.Frame(
        notebook
    )


    # --------------------------------------------------------------------------
    # 4. AGREGAR LAS PESTAÑAS AL NOTEBOOK
    # --------------------------------------------------------------------------

    # notebook.add() agrega cada Frame como una pestaña.

    notebook.add(
        pestana_clientes,
        text="Clientes"
    )


    notebook.add(
        pestana_empleados,
        text="Empleados"
    )


    notebook.add(
        pestana_proveedores,
        text="Proveedores"
    )


    notebook.add(
        pestana_stock,
        text="Stock"
    )


    notebook.add(
        pestana_facturacion,
        text="Facturación"
    )


    # ==========================================================================
    # 5. CONSTRUIR EL CONTENIDO DE CADA PESTAÑA
    # ==========================================================================

    # CAMBIO FUNDAMENTAL
    # --------------------------------------------------------------------------
    #
    # Este es el bloque que faltaba.
    #
    # Hasta ahora interfaz.py hacía:
    #
    #     crear pestaña
    #          ↓
    #     colocar "Ficha de Clientes"
    #
    # Ahora hacemos:
    #
    #     crear pestaña
    #          ↓
    #     entregar pestaña al módulo correspondiente
    #          ↓
    #     el módulo construye su contenido
    #
    #
    # Cada clase recibe la pestaña que interfaz.py ya creó.
    #
    # Por ejemplo:
    #
    #     Clientes(pestana_clientes)
    #
    # significa:
    #
    #     "Clientes, construye tu interfaz dentro de esta pestaña".


    # --------------------------------------------------------------------------
    # CLIENTES
    # --------------------------------------------------------------------------

    Clientes(
        pestana_clientes
    )


    # --------------------------------------------------------------------------
    # EMPLEADOS
    # --------------------------------------------------------------------------

    Empleados(
        pestana_empleados
    )


    # --------------------------------------------------------------------------
    # PROVEEDORES
    # --------------------------------------------------------------------------

    Proveedores(
        pestana_proveedores
    )


    # --------------------------------------------------------------------------
    # STOCK
    # --------------------------------------------------------------------------

    Stock(
        pestana_stock
    )


    # --------------------------------------------------------------------------
    # FACTURACIÓN
    # --------------------------------------------------------------------------

    Facturacion(
        pestana_facturacion
    )


    # ==========================================================================
    # 6. BUCLE PRINCIPAL
    # ==========================================================================

    # mainloop() mantiene abierta la ventana y espera
    # las acciones del usuario.
    #
    # Es el único mainloop() de todo nuestro proyecto.
    #
    # Mientras mainloop() está funcionando:
    #
    #     usuario hace algo
    #          ↓
    #     Tkinter detecta el evento
    #          ↓
    #     ejecuta la función correspondiente

    ventana.mainloop()