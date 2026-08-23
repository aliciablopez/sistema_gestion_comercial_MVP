# clientes.py
# Este módulo contiene todo lo relacionado con la pestaña Clientes:
#   - formulario de carga
#   - tabla de clientes
#   - operaciones CRUD

# IMPORTANTE:
# Este archivo NO crea la ventana principal de Tkinter. Tampoco contiene mainloop(). La ventana principal y el Notebook pertenecen a interfaz.py.

# ==============================================================================
# 1. IMPORTACIONES
# ==============================================================================

import tkinter as tk # trae interfaz gráfica
from tkinter import ttk # permite hacer tablas
from tkinter import messagebox # permite mostrar mensajes al usuario

# ==============================================================================
# 2. CREAR LA PESTAÑA DE CLIENTES
# ==============================================================================

def crear_pestana_clientes(notebook):
    # --------------------------------------------------------------------------
    # CREAMOS EL FRAME
    # --------------------------------------------------------------------------
    #
    # Una pestaña de Notebook necesita ser un widget. tk.Frame funciona como un "contenedor" donde colocaremos:
    #   - etiquetas (label)
    #   - Entry     (caja de texto)
    #   - botones (clicables
    #   - Treeview (tabla de clientes y otros MM)
    #
    # El Notebook pertenece a interfaz.py. Aquí solamente recibimos ese Notebook como argumento.
    # --------------------------------------------------------------------------

    pestana = tk.Frame(notebook)

    # Agregamos el Frame como una nueva pestaña del Notebook.
    notebook.add(
        pestana,
        text="Clientes"
    )

    # ==========================================================================
    # 3. FORMULARIO
    # ==========================================================================

    # --------------------------------------------------------------------------
    # RAZÓN SOCIAL
    # --------------------------------------------------------------------------
    tk.Label(
        pestana,
        text="Razón Social:"
    ).grid(
        row=0,
        column=0,
        padx=5,
        pady=4,
        sticky="e"
    )

    caja_razon_social = tk.Entry(
        pestana,
        width=25
    )

    caja_razon_social.grid(
        row=0,
        column=1,
        padx=5,
        pady=4
    )

    # --------------------------------------------------------------------------
    # CONTACTO
    # --------------------------------------------------------------------------

    tk.Label(
        pestana,
        text="Contacto:"
    ).grid(
        row=1,
        column=0,
        padx=5,
        pady=4,
        sticky="e"
    )

    caja_contacto = tk.Entry(
        pestana,
        width=25
    )

    caja_contacto.grid(
        row=1,
        column=1,
        padx=5,
        pady=4
    )

    # --------------------------------------------------------------------------
    # CUIT
    # --------------------------------------------------------------------------

    tk.Label(
        pestana,
        text="CUIT:"
    ).grid(
        row=2,
        column=0,
        padx=5,
        pady=4,
        sticky="e"
    )

    caja_cuit = tk.Entry(
        pestana,
        width=25
    )

    caja_cuit.grid(
        row=2,
        column=1,
        padx=5,
        pady=4
    )

    # ==========================================================================
    # 4. TABLA DE CLIENTES
    # ==========================================================================

    # Definimos las columnas de la tabla.
    columnas = (
        "Razón Social",
        "Contacto",
        "CUIT"
    )

    # Creamos el Treeview.
    tabla = ttk.Treeview(
        pestana,
        columns=columnas,
        show="headings",
        height=10
    )

    # Ancho de cada columna.
    anchos = [250, 200, 150]

    # Configuramos los encabezados y las columnas.
    for indice, columna in enumerate(columnas):

        tabla.heading(
            columna,
            text=columna
        )

        tabla.column(
            columna,
            width=anchos[indice],
            anchor="center"
        )


    # Colocamos la tabla debajo del formulario.
    tabla.grid(
        row=6,
        column=0,
        columnspan=5,
        padx=15,
        pady=(10, 15),
        sticky="ew"
    )


    # ==========================================================================
    # 5. FUNCIONES CRUD
    # ==========================================================================

    # --------------------------------------------------------------------------
    # LIMPIAR CAMPOS
    # --------------------------------------------------------------------------

    def limpiar_campos():

        caja_razon_social.delete(
            0,
            tk.END
        )

        caja_contacto.delete(
            0,
            tk.END
        )

        caja_cuit.delete(
            0,
            tk.END
        )


    # --------------------------------------------------------------------------
    # NUEVO CLIENTE
    # --------------------------------------------------------------------------

    def nuevo_cliente():

        # Dejamos el formulario vacío.
        limpiar_campos()

        # Quitamos la selección de la tabla.
        tabla.selection_remove(
            tabla.selection()
        )

        # Colocamos el cursor en el primer campo.
        caja_razon_social.focus()


    # --------------------------------------------------------------------------
    # CARGAR DATOS SELECCIONADOS
    # --------------------------------------------------------------------------

    def cargar_datos_seleccionados():

        # Obtenemos la fila seleccionada.
        seleccion = tabla.selection()

        # Si no hay ninguna fila seleccionada, terminamos.
        if not seleccion:
            return

        # Obtenemos el identificador de la fila.
        item_id = seleccion[0]

        # Obtenemos los valores de esa fila.
        valores = tabla.item(
            item_id,
            "values"
        )

        # Pasamos los datos de la tabla al formulario.
        limpiar_campos()

        caja_razon_social.insert(
            0,
            valores[0]
        )

        caja_contacto.insert(
            0,
            valores[1]
        )

        caja_cuit.insert(
            0,
            valores[2]
        )


    # --------------------------------------------------------------------------
    # GUARDAR CLIENTE
    # --------------------------------------------------------------------------

    def guardar():

        # Obtenemos los datos del formulario.
        razon_social = caja_razon_social.get().strip()
        contacto = caja_contacto.get().strip()
        cuit = caja_cuit.get().strip()


        # Validamos los campos obligatorios.
        if not razon_social or not cuit:

            messagebox.showerror(
                "Error",
                "Razón Social y CUIT son obligatorios.",
                parent=pestana
            )

            return


        # Validamos que el CUIT contenga solamente números.
        if not cuit.isdigit():

            messagebox.showerror(
                "Error",
                "El CUIT debe contener solamente números.",
                parent=pestana
            )
            return

        # Comprobamos que el CUIT no esté repetido.
        for item in tabla.get_children():

            valores = tabla.item(
                item,
                "values"
            )

            if valores[2] == cuit:

                messagebox.showerror(
                    "Error",
                    "Ya existe un cliente con ese CUIT.",
                    parent=pestana
                )
                return

        # Agregamos el cliente a la tabla.
        tabla.insert(
            "",
            "end",
            values=(
                razon_social,
                contacto,
                cuit
            )
        )

        # Informamos que la operación terminó correctamente.
        messagebox.showinfo(
            "Éxito",
            "Cliente guardado.",
            parent=pestana
        )

        # Dejamos preparado el formulario para otro cliente.
        limpiar_campos()

    # --------------------------------------------------------------------------
    # MODIFICAR CLIENTE
    # --------------------------------------------------------------------------

    def modificar():

        # Buscamos la fila seleccionada.
        seleccion = tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Atención",
                "Selecciona un cliente para modificar.",
                parent=pestana
            )
            return

        # Obtenemos el identificador y los valores actuales.
        item_id = seleccion[0]

        valores = tabla.item(
            item_id,
            "values"
        )

        # ----------------------------------------------------------------------
        # VENTANA EMERGENTE DE EDICIÓN
        # ----------------------------------------------------------------------

        ventana_edicion = tk.Toplevel(
            pestana
        )

        ventana_edicion.title(
            "Modificar Cliente"
        )

        ventana_edicion.geometry(
            "400x280"
        )

        ventana_edicion.resizable(
            False,
            False
        )

        # La ventana queda asociada a la pestaña.
        ventana_edicion.transient(
            pestana
        )

        # El usuario debe terminar la edición antes de volver a trabajar con la pestaña.
        ventana_edicion.grab_set()

        # ----------------------------------------------------------------------
        # CAMPOS DE EDICIÓN
        # ----------------------------------------------------------------------

        tk.Label(
            ventana_edicion,
            text="Modificar datos del cliente",
            font=("Arial", 12, "bold")
        ).pack(
            pady=(15, 10)
        )

        tk.Label(
            ventana_edicion,
            text="Razón Social:"
        ).pack(
            anchor="w",
            padx=30
        )

        caja_razon_edicion = tk.Entry(
            ventana_edicion,
            width=40
        )

        caja_razon_edicion.pack(
            padx=30,
            pady=(2, 8)
        )

        caja_razon_edicion.insert(
            0,
            valores[0]
        )

        tk.Label(
            ventana_edicion,
            text="Contacto:"
        ).pack(
            anchor="w",
            padx=30
        )


        caja_contacto_edicion = tk.Entry(
            ventana_edicion,
            width=40
        )

        caja_contacto_edicion.pack(
            padx=30,
            pady=(2, 8)
        )

        caja_contacto_edicion.insert(
            0,
            valores[1]
        )

        tk.Label(
            ventana_edicion,
            text="CUIT:"
        ).pack(
            anchor="w",
            padx=30
        )


        caja_cuit_edicion = tk.Entry(
            ventana_edicion,
            width=40
        )

        caja_cuit_edicion.pack(
            padx=30,
            pady=(2, 12)
        )

        caja_cuit_edicion.insert(
            0,
            valores[2]
        )

        # ----------------------------------------------------------------------
        # GUARDAR MODIFICACIÓN
        # ----------------------------------------------------------------------

        def guardar_modificacion():

            razon_social = caja_razon_edicion.get().strip()
            contacto = caja_contacto_edicion.get().strip()
            cuit = caja_cuit_edicion.get().strip()

            if not razon_social or not cuit:

                messagebox.showerror(
                    "Error",
                    "Razón Social y CUIT son obligatorios.",
                    parent=ventana_edicion
                )
                return

            if not cuit.isdigit():

                messagebox.showerror(
                    "Error",
                    "El CUIT debe contener solamente números.",
                    parent=ventana_edicion
                )
                return

            # Comprobamos que el CUIT no pertenezca a otro cliente.
            for item in tabla.get_children():

                if item == item_id:
                    continue

                valores_otro = tabla.item(
                    item,
                    "values"
                )

                if valores_otro[2] == cuit:

                    messagebox.showerror(
                        "Error",
                        "Ya existe otro cliente con ese CUIT.",
                        parent=ventana_edicion
                    )
                    return

            # Actualizamos la fila seleccionada.
            tabla.item(
                item_id,
                values=(
                    razon_social,
                    contacto,
                    cuit
                )
            )

            # Cerramos la ventana de edición.
            ventana_edicion.destroy()

            messagebox.showinfo(
                "Éxito",
                "El cliente fue modificado correctamente.",
                parent=pestana
            )

        # ----------------------------------------------------------------------
        # BOTONES DE LA VENTANA DE EDICIÓN
        # ----------------------------------------------------------------------

        marco_botones = tk.Frame(
            ventana_edicion
        )

        marco_botones.pack(
            pady=5
        )


        tk.Button(
            marco_botones,
            text="Guardar cambios",
            command=guardar_modificacion,
            width=16
        ).pack(
            side="left",
            padx=5
        )


        tk.Button(
            marco_botones,
            text="Cancelar",
            command=ventana_edicion.destroy,
            width=12
        ).pack(
            side="left",
            padx=5
        )

        caja_razon_edicion.focus()

    # --------------------------------------------------------------------------
    # ELIMINAR CLIENTE
    # --------------------------------------------------------------------------

    def eliminar():

        seleccion = tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Atención",
                "Selecciona un cliente para eliminar.",
                parent=pestana
            )
            return

        item_id = seleccion[0]

        valores = tabla.item(
            item_id,
            "values"
        )

        razon_social = valores[0]
        contacto = valores[1]
        cuit = valores[2]

        # Pedimos confirmación antes de eliminar.
        confirmar = messagebox.askyesno(
            "Confirmar baja",
            f"¿Deseas eliminar este cliente?\n\n"
            f"Razón Social: {razon_social}\n"
            f"Contacto: {contacto}\n"
            f"CUIT: {cuit}\n\n"
            f"Esta operación no se puede deshacer.",
            parent=pestana
        )

        if confirmar:

            tabla.delete(
                item_id
            )

            limpiar_campos()

            messagebox.showinfo(
                "Baja realizada",
                "El cliente fue eliminado correctamente.",
                parent=pestana
            )

    # ==========================================================================
    # 6. ENLACE DEL EVENTO DE SELECCIÓN
    # ==========================================================================

    # Cuando el usuario selecciona una fila se cargan sus datos en el formulario.
    tabla.bind(
        "<<TreeviewSelect>>",
        cargar_datos_seleccionados
    )

    # ==========================================================================
    # 7. BOTONES CRUD
    # ==========================================================================

    tk.Button(
        pestana,
        text="Nuevo Cliente",
        command=nuevo_cliente,
        width=16
    ).grid(
        row=0,
        column=4,
        padx=15,
        pady=2
    )

    tk.Button(
        pestana,
        text="Guardar Cliente",
        command=guardar,
        width=16
    ).grid(
        row=1,
        column=4,
        padx=15,
        pady=2
    )

    tk.Button(
        pestana,
        text="Modificar Cliente",
        command=modificar,
        width=16
    ).grid(
        row=2,
        column=4,
        padx=15,
        pady=2
    )

    tk.Button(
        pestana,
        text="Eliminar Cliente",
        command=eliminar,
        width=16
    ).grid(
        row=3,
        column=4,
        padx=15,
        pady=2
    )

    # ==========================================================================
    # 8. RESULTADO DE LA FUNCIÓN
    # ==========================================================================

    # Devolvemos la pestaña creada. Esto permite que interfaz.py pueda conservar una referencia
    # al Frame si posteriormente necesitamos trabajar con él.
    return pestana