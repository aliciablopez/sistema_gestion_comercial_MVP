# ==============================================================================
# INTERFAZ DE LA APLICACIÓN
# ==============================================================================

# tkinter contiene los elementos básicos de la interfaz gráfica.
import tkinter as tk

# ttk contiene widgets con una apariencia más moderna. En este ejercicio utilizaremos Notebook y Frame.
from tkinter import ttk

# ==============================================================================
# FUNCIÓN PRINCIPAL DE LA INTERFAZ
# ==============================================================================

def iniciar_aplicacion():

    # --------------------------------------------------------------------------
    # 1. CREAR LA VENTANA PRINCIPAL
    # --------------------------------------------------------------------------

    # tk.Tk() crea la ventana raíz de la aplicación.
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión Comercial")
    ventana.geometry("900x600")

    # Evitamos que el usuario cambie el tamaño de la ventana.
    ventana.resizable(False, False)


    # --------------------------------------------------------------------------
    # 2. CREAR EL NOTEBOOK
    # --------------------------------------------------------------------------

    # Notebook es un widget de ttk que permite organizar diferentes contenidos mediante pestañas.
    notebook = ttk.Notebook(ventana)

    # Colocamos el Notebook dentro de la ventana principal.
    notebook.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # --------------------------------------------------------------------------
    # 3. CREAR LAS PESTAÑAS
    # --------------------------------------------------------------------------

    # Cada pestaña será un Frame. Un Frame es un widget contenedor: permite colocar dentro otros widgets.
    pestana_clientes = ttk.Frame(notebook)
    pestana_empleados = ttk.Frame(notebook)
    pestana_proveedores = ttk.Frame(notebook)
    pestana_stock = ttk.Frame(notebook)
    pestana_facturacion = ttk.Frame(notebook)

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


    # --------------------------------------------------------------------------
    # 5. CONTENIDO PROVISORIO DE LAS PESTAÑAS
    # --------------------------------------------------------------------------

    # Por ahora colocamos solamente un texto. Más adelante cada pestana tendrá su propia interfaz.
    ttk.Label(
        pestana_clientes,
        text="Ficha de Clientes"
    ).pack(pady=30)

    ttk.Label(
        pestana_empleados,
        text="Ficha de Empleados"
    ).pack(pady=30)

    ttk.Label(
        pestana_proveedores,
        text="Ficha de Proveedores"
    ).pack(pady=30)

    ttk.Label(
        pestana_stock,
        text="Ficha de Stock"
    ).pack(pady=30)

    ttk.Label(
        pestana_facturacion,
        text="Emisión de Facturación"
    ).pack(pady=30)


    # --------------------------------------------------------------------------
    # 6. BUCLE PRINCIPAL
    # --------------------------------------------------------------------------

    # mainloop() mantiene abierta la ventana y espera las acciones del usuario.
    ventana.mainloop()